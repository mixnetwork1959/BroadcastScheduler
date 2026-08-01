# ==========================================
# Broadcast Scheduler
# Version 4.5.1
# schedule_engine.py
# ==========================================

from datetime import datetime, timedelta
from typing import List

from models import Event, RunTime


class ScheduleEngine:

    def __init__(self):
        self.week_start = None
        self.week_end = None

    def get_current_week(self, week_offset: int = 0):
        today = datetime.now()

        monday = today - timedelta(days=today.weekday())
        monday += timedelta(weeks=week_offset)
        monday = monday.replace(hour=0, minute=0, second=0, microsecond=0)

        sunday = monday + timedelta(days=6)
        sunday = sunday.replace(hour=23, minute=59, second=59, microsecond=0)

        self.week_start = monday
        self.week_end = sunday

        return monday, sunday

    def decode_days(self, days: str) -> List[int]:
        result = []
        if len(days) != 7:
            return result

        mapping = [6, 0, 1, 2, 3, 4, 5]

        for index, value in enumerate(days):
            if value == "1":
                result.append(mapping[index])

        return sorted(result)

    def decode_hours(self, hours: str) -> List[int]:
        return [hour for hour, value in enumerate(hours) if value == "1"]

    def decode_minutes(self, minutes: str) -> List[int]:
        if not minutes:
            return [0]

        result = []
        for value in minutes.split(","):
            value = value.strip()
            if value:
                result.append(int(value))
        return result

    def decode_seconds(self, seconds: int) -> int:
        return seconds

    def parse_event_datetime(self, value: str):
        """Parse RadioBOSS DateTime values without failing the schedule."""

        value = (value or "").strip()

        for format_string in (
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M",
            "%Y-%m-%d",
        ):
            try:
                return datetime.strptime(value, format_string)
            except ValueError:
                continue

        return None

    def _event_times(self, event: Event):
        """Return the configured launch times for one event."""

        event_datetime = self.parse_event_datetime(event.datetime)

        # RadioBOSS TimeType 1 uses the Hours/Minutes controls.
        if event.time_type == 1:
            hours = self.decode_hours(event.hours)
            minutes = self.decode_minutes(event.minutes)
            second = self.decode_seconds(event.seconds)
            return [
                (hour, minute, second)
                for hour in hours
                for minute in minutes
            ]

        # The regular Time control stores its value in DateTime.
        if event_datetime is not None:
            return [(
                event_datetime.hour,
                event_datetime.minute,
                event_datetime.second,
            )]

        return []

    def _dated_event_days(self, event: Event):
        """Return fixed or annually recurring dates inside the shown week."""

        event_datetime = self.parse_event_datetime(event.datetime)

        if event_datetime is None:
            return []

        candidates = []

        if event.every_year:
            years = {
                self.week_start.year,
                self.week_end.year,
            }

            for year in years:
                try:
                    candidates.append(
                        event_datetime.replace(year=year)
                    )
                except ValueError:
                    # A 29 February event does not exist in every year.
                    continue
        else:
            candidates.append(event_datetime)

        return [
            candidate
            for candidate in candidates
            if self.week_start.date()
            <= candidate.date()
            <= self.week_end.date()
        ]

    def _generate_event(self, event: Event) -> List[RunTime]:
        runtimes: List[RunTime] = []

        if not event.enabled:
            return runtimes

        times = self._event_times(event)

        if not times:
            return runtimes

        # A date without weekday scheduling is a one-off or annual event.
        # The Days mask is irrelevant in this RadioBOSS mode.
        if event.use_date and not event.use_days_of_week:
            current_days = self._dated_event_days(event)
        elif event.use_days_of_week:
            current_days = [
                self.week_start + timedelta(days=weekday)
                for weekday in self.decode_days(event.days)
            ]

            # When Date and weekdays are combined, Date is the first day on
            # which the recurring weekday schedule may run.
            if event.use_date and not event.every_year:
                first_date = self.parse_event_datetime(event.datetime)
                if first_date is not None:
                    current_days = [
                        day
                        for day in current_days
                        if day.date() >= first_date.date()
                    ]
        else:
            current_days = []

        for current_day in current_days:
            for hour, minute, second in times:
                start = current_day.replace(
                    hour=hour,
                    minute=minute,
                    second=second,
                    microsecond=0
                )

                runtimes.append(
                    RunTime(
                        event=event,
                        start=start,
                        end=start
                    )
                )

        return runtimes

    def generate(
        self,
        events: List[Event],
        week_offset: int = 0
    ) -> List[RunTime]:

        self.get_current_week(week_offset)

        runtimes: List[RunTime] = []

        for event in events:
            event_runtimes = self._generate_event(event)
            runtimes.extend(event_runtimes)

        runtimes.sort(key=lambda rt: rt.start)

        for current, nxt in zip(runtimes, runtimes[1:]):
            current.end = nxt.start

        if runtimes:
            runtimes[-1].end = self.week_end

        return runtimes

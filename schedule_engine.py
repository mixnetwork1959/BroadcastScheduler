# ==========================================
# Broadcast Scheduler
# Version 2.1.0
# schedule_engine.py
#
# Teil 1
# ==========================================

from datetime import datetime, timedelta
from typing import List

from models import Event, RunTime


class ScheduleEngine:

    def __init__(self):

        self.week_start = None
        self.week_end = None

    # -------------------------------------------------
    # Aktuelle Kalenderwoche
    # -------------------------------------------------

    def get_current_week(self):

        today = datetime.now()

        monday = today - timedelta(days=today.weekday())

        monday = monday.replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

        sunday = monday + timedelta(days=6)

        sunday = sunday.replace(
            hour=23,
            minute=59,
            second=59,
            microsecond=0
        )

        self.week_start = monday
        self.week_end = sunday

        return monday, sunday

    # -------------------------------------------------
    # Days
    # 1111111
    # -------------------------------------------------

    def decode_days(self, days: str) -> List[int]:

        result = []

        if len(days) != 7:
            return result

        # SDL:
        # Su Mo Tu We Th Fr Sa
        mapping = [6, 0, 1, 2, 3, 4, 5]

        for index, value in enumerate(days):

            if value == "1":
                result.append(mapping[index])

        return sorted(result)

    # -------------------------------------------------
    # Hours
    # 000000111100000000000000
    # -------------------------------------------------

    def decode_hours(self, hours: str) -> List[int]:

        result = []

        for hour, value in enumerate(hours):

            if value == "1":
                result.append(hour)

        return result

    # -------------------------------------------------
    # Minutes
    # 17,43
    # -------------------------------------------------

    def decode_minutes(self, minutes: str) -> List[int]:

        if not minutes:
            return [0]

        result = []

        for value in minutes.split(","):

            value = value.strip()

            if value == "":
                continue

            result.append(int(value))

        return result

    # -------------------------------------------------
    # Seconds
    # -------------------------------------------------

    def decode_seconds(self, seconds: int) -> int:

        return seconds
		    # -------------------------------------------------
    # Erzeugt alle RunTimes eines Events
    # (TimeType = 1)
    # -------------------------------------------------

    def _generate_event(self, event: Event) -> List[RunTime]:

        runtimes: List[RunTime] = []

        # Nur aktivierte Events
        if not event.enabled:
            return runtimes

        # Nur Wochen-Events
        if event.time_type != 1:
            return runtimes

        days = self.decode_days(event.days)
        hours = self.decode_hours(event.hours)
        minutes = self.decode_minutes(event.minutes)
        second = self.decode_seconds(event.seconds)

        for weekday in days:

            current_day = self.week_start + timedelta(days=weekday)

            for hour in hours:

                for minute in minutes:

                    start = current_day.replace(
                        hour=hour,
                        minute=minute,
                        second=second,
                        microsecond=0
                    )

                    runtime = RunTime(
                        event=event,
                        start=start,
                        end=start
                    )

                    runtimes.append(runtime)

        return runtimes
		    # -------------------------------------------------
    # Erzeugt den Wochenplan
    # -------------------------------------------------

    def generate(self, events: List[Event]) -> List[RunTime]:

        # Aktuelle Woche bestimmen
        self.get_current_week()

        print()
        print("=" * 45)
        print("Aktuelle Kalenderwoche")
        print("=" * 45)
        print(f"Von : {self.week_start.strftime('%d.%m.%Y')}")
        print(f"Bis : {self.week_end.strftime('%d.%m.%Y')}")
        print("=" * 45)
        print()

        runtimes: List[RunTime] = []

        for event in events:

            runtimes.extend(
                self._generate_event(event)
            )

        # Nach Datum/Uhrzeit sortieren
        runtimes.sort(key=lambda rt: rt.start)

        return runtimes
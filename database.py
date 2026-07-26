# ==========================================
# Broadcast Scheduler
# Version 2.0.2
# database.py
#
# Änderungen:
# - Minutes jetzt als String
# - Seconds bleibt Integer
# - An models.py 2.0.2 angepasst
# ==========================================

import os
from typing import List

from models import Event


class Database:

    def __init__(self, settings):

        self.settings = settings
        self.filename = settings.get("admin_sdl", "")

    def load_events(self) -> List[Event]:

        if not os.path.exists(self.filename):
            raise FileNotFoundError(self.filename)

        events: List[Event] = []

        current = None

        with open(self.filename, "r", encoding="utf-8", errors="ignore") as f:

            for line in f:

                line = line.strip()

                if not line:
                    continue

                if line.lower().startswith("[event"):

                    if current:
                        events.append(Event(**current))

                    current = {
                        "id": "",
                        "name": "",
                        "filename": "",
                        "group": "",
                        "enabled": False,
                        "datetime": "",
                        "use_date": False,
                        "every_year": False,
                        "use_days_of_week": False,
                        "days": "",
                        "hours": "",
                        "minutes": "",
                        "seconds": 0,
                        "time_type": 0,
                        "immediately": False,
                        "repeat": 0,
                        "repeat_period": 0,
                        "repeat_count": 0,
                        "repeat_limit": 0
                    }

                    continue

                if current is None:
                    continue

                if "=" not in line:
                    continue

                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip()

                if key == "ID":
                    current["id"] = value
                elif key == "TaskName":
                    current["name"] = value
                elif key == "FileName":
                    current["filename"] = value
                elif key == "GroupName":
                    current["group"] = value
                elif key == "EnabledEvent":
                    current["enabled"] = (value == "1")
                elif key == "DateTime":
                    current["datetime"] = value
                elif key == "UseDate":
                    current["use_date"] = (value == "1")
                elif key == "EveryYear":
                    current["every_year"] = (value == "1")
                elif key == "UseDaysOfWeek":
                    current["use_days_of_week"] = (value == "1")
                elif key == "Days":
                    current["days"] = value
                elif key == "Hours":
                    current["hours"] = value
                elif key == "Minutes":
                    current["minutes"] = value
                elif key == "Seconds":
                    current["seconds"] = int(value) if value else 0
                elif key == "TimeType":
                    current["time_type"] = int(value) if value else 0
                elif key == "Immediately":
                    current["immediately"] = (value == "1")
                elif key == "Repeat":
                    current["repeat"] = int(value) if value else 0
                elif key == "RepeatPeriod":
                    current["repeat_period"] = int(value) if value else 0
                elif key == "RepeatCount":
                    current["repeat_count"] = int(value) if value else 0
                elif key == "RepeatLimit":
                    current["repeat_limit"] = int(value) if value else 0
            
            if current:
                events.append(Event(**current))

            return events

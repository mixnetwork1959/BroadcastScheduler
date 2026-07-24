# ==========================================
# Broadcast Scheduler
# Version 0.1.1
# parser.py
# ==========================================

import os

DAY_NAMES = [
    "Su",
    "Mo",
    "Tu",
    "We",
    "Th",
    "Fr",
    "Sa"
]


def decode_days(days):
    """1111111 -> ['Su','Mo','Tu',...]"""

    result = []

    for i, value in enumerate(days):
        if value == "1":
            result.append(DAY_NAMES[i])

    return result


def decode_hours(hours):
    """000000111100000000000000 -> [6,7,8,9]"""

    result = []

    for hour, value in enumerate(hours):
        if value == "1":
            result.append(hour)

    return result


def build_time_blocks(hour_list):
    """
    Wandelt eine Stundenliste in Zeitblöcke um.

    Beispiele:

    [6,7,8,9]
        -> [("06:00","10:00")]

    [22,23,0,1,2,3,4,5]
        -> [("22:00","06:00")]

    [0..23]
        -> [("00:00","24:00")]
    """

    if not hour_list:
        return []

    # Alle 24 Stunden
    if len(hour_list) == 24:
        return [("00:00", "24:00")]

    # Über Mitternacht (Night)
    if 0 in hour_list and 23 in hour_list:

        start = min(h for h in hour_list if h >= 12)
        end = max(h for h in hour_list if h < 12) + 1

        return [
            (
                f"{start:02d}:00",
                f"{end:02d}:00"
            )
        ]

    blocks = []

    start = hour_list[0]
    previous = hour_list[0]

    for hour in hour_list[1:]:

        if hour == previous + 1:
            previous = hour
            continue

        blocks.append(
            (
                f"{start:02d}:00",
                f"{previous+1:02d}:00"
            )
        )

        start = hour
        previous = hour

    blocks.append(
        (
            f"{start:02d}:00",
            f"{previous+1:02d}:00"
        )
    )

    return blocks


def load_events(filename):

    if not os.path.exists(filename):
        raise FileNotFoundError(filename)

    events = []

    current = None

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            if line.startswith("[event"):

                if current:

                    current["DayList"] = decode_days(current["Days"])
                    current["HourList"] = decode_hours(current["Hours"])
                    current["TimeBlocks"] = build_time_blocks(
                    current["HourList"]
                    )
                    print("-" * 40)
                    events.append(current)

                current = {
                    "TaskName": "",
                    "EnabledEvent": "0",
                    "Days": "",
                    "Hours": "",
                    "Minutes": ""
                }

                continue

            if current is None:
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)

            key = key.strip()
            value = value.strip()

            if key in current:
                current[key] = value

    if current:

        current["DayList"] = decode_days(current["Days"])
        current["HourList"] = decode_hours(current["Hours"])
        current["TimeBlocks"] = build_time_blocks(
            current["HourList"]
        )

        events.append(current)

    return events
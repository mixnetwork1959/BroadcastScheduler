# ==========================================
# Broadcast Scheduler
# Version 2.0.2
# models.py
#
# Änderungen:
# - minutes von int -> str geändert
# - seconds bleibt int
# ==========================================

from dataclasses import dataclass
from datetime import datetime


# ==========================================
# Event aus der RadioBOSS Admin.sdl
# ==========================================

@dataclass
class Event:

    id: str

    # Allgemein
    name: str
    filename: str
    group: str

    enabled: bool

    # Datum / Zeit
    datetime: str
    use_date: bool
    every_year: bool

    # Wochentage / Uhrzeit
    use_days_of_week: bool
    days: str
    hours: str
    minutes: str
    seconds: int

    # Ausführungsart
    time_type: int
    immediately: bool

    # Wiederholung
    repeat: int
    repeat_period: int
    repeat_count: int
    repeat_limit: int


# ==========================================
# Berechneter Ausführungszeitpunkt
# ==========================================

@dataclass
class RunTime:

    event: Event

    start: datetime
    end: datetime
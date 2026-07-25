# ==========================================
# Broadcast Scheduler
# Version 2.0.0
# scheduler.py
# ==========================================

from config import load_settings
from database import Database
from schedule_engine import ScheduleEngine
from gui import show_events

VERSION = "2.0.0"


def main():

    print("=" * 45)
    print(f" Broadcast Scheduler v{VERSION}")
    print("=" * 45)

    # Einstellungen laden
    settings = load_settings()

    # Datenbank öffnen
    db = Database(settings)

    # Events laden
    events = db.load_events()
    print(f"Events geladen: {len(events)}")

    # Wochenplan erzeugen
    engine = ScheduleEngine()
    runtimes = engine.generate(events)
    print(f"RunTimes erzeugt: {len(runtimes)}")

    # GUI starten
    show_events(runtimes)


if __name__ == "__main__":
    main()
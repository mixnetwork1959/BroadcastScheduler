# ==========================================
# Broadcast Scheduler
# Version 2.5.0
# scheduler.py
# ==========================================

from config import load_settings
from database import Database
from schedule_engine import ScheduleEngine
from analyzer import Analyzer
from gui import show_events

VERSION = "2.5.0"


def main():

    print("=" * 45)
    print(f" Broadcast Scheduler v{VERSION}")
    print("=" * 45)

    # Load settings
    settings = load_settings()

    # Open database
    db = Database(settings)

    # Load events
    events = db.load_events()
    print(f"Events loaded: {len(events)}")

    # Generate schedule
    engine = ScheduleEngine()
    runtimes = engine.generate(events)
    print(f"RunTimes generated: {len(runtimes)}")

    # Analyze schedule
    analyzer = Analyzer(runtimes)
    runtimes = analyzer.analyze()

    print("Schedule analysis completed.")

    # Start GUI
    show_events(runtimes)


if __name__ == "__main__":
    main()
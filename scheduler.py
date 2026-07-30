# ==========================================
# Broadcast Scheduler
# Version 4.4.0
# scheduler.py
# ==========================================

from config import load_settings
from database import Database
from scheduler_controller import SchedulerController
from gui import show_events

VERSION = "4.4.0"


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

    # Create controller
    controller = SchedulerController(events)

    # Generate current week
    runtimes = controller.refresh()
    print(f"RunTimes generated: {len(runtimes)}")

    print("Schedule analysis completed.")

    # Start GUI
    show_events(
        controller,
        runtimes,
        settings
    )


if __name__ == "__main__":
    main()

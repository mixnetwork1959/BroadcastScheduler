# ==========================================
# Broadcast Scheduler
# Version 0.2.3
# scheduler.py
# ==========================================

from config import load_settings
from parser import load_events
from gui import show_events

VERSION = "0.2.3"


def main():

    print("=" * 45)
    print(f" Broadcast Scheduler v{VERSION}")
    print("=" * 45)

    settings = load_settings()

    filename = settings.get("admin_sdl", "")

    if not filename:
        print()
        print("Bitte den Pfad zur Admin.sdl in der")
        print("settings.json eintragen.")
        return

    try:
        events = load_events(filename)

    except Exception as e:
        print()
        print("Fehler:")
        print(e)
        return

    # GUI starten
    show_events(
        filename=filename,
        events=events,
        version=VERSION
    )


if __name__ == "__main__":
    main()
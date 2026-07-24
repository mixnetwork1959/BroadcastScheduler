# ==========================================
# Broadcast Scheduler
# Version 0.1.0
# config.py
# ==========================================

import json
import os

SETTINGS_FILE = "settings.json"


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {
            "admin_sdl": ""
        }

    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)
# 📅 Broadcast Scheduler

╔══════════════════════════════════════════════╗
║            📅 Broadcast Scheduler            ║
║        RadioBOSS Schedule Analyzer           ║
╚══════════════════════════════════════════════╝
![Version](https://img.shields.io/badge/version-2.3.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.14-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Broadcast Scheduler ist ein Analyse- und Planungswerkzeug für **RadioBOSS**.

Das Programm liest die originale **Admin.sdl** von RadioBOSS ein und erzeugt daraus einen übersichtlichen Wochenplan. Dadurch lassen sich Sendeabläufe kontrollieren, Fehler erkennen und Programmschemata überprüfen.

---

# ✨ Funktionen

## Bereits verfügbar

- ✅ Admin.sdl einlesen
- ✅ RadioBOSS Events analysieren
- ✅ Wochenplan erzeugen
- ✅ Aktuelle Kalenderwoche automatisch erkennen
- ✅ Sortierbare Tabelle
- ✅ Vertikale und horizontale Scrollbars
- ✅ Toolbar
- ✅ Statusleiste
- ✅ Unterstützung mehrerer Minuten (z.B. 17,43)

---

# 🚧 Geplante Funktionen

## Version 2.4

- Gruppen anzeigen
- Toolbar erweitern
- Doppelklick auf Events
- bessere Statusleiste
- Detailfenster

## Version 2.5

- Monatsansicht
- Wochennavigation
- Konflikterkennung
- Programmlücken erkennen
- Überschneidungen erkennen

## Version 3.0

- PDF Export
- CSV Export
- Druckfunktion
- Suchfunktion
- Filter
- Farbige Eventtypen

---

# 🖥 Screenshot


![Broadcast Scheduler](screenshot_01.PNG)

---

# 📂 Projektstruktur

```
BroadcastScheduler
│
├── checker.py
├── config.py
├── database.py
├── gui.py
├── LICENSE
├── models.py
├── parser.py
├── schedule_engine.py
├── scheduler.py
├── settings.example.json
└── README.md
```

---

# ⚙ Voraussetzungen

- Windows 10 / Windows 11
- Python 3.14 oder neuer
- RadioBOSS

---

# 🚀 Installation

Repository klonen

```bash
git clone https://github.com/mixnetwork1959/BroadcastScheduler.git
```

Projektordner öffnen

```bash
cd BroadcastScheduler
```

Datei

```
settings.example.json
```

kopieren nach

```
settings.json
```

und den Pfad zur eigenen **Admin.sdl** eintragen.

Beispiel:

```json
{
    "admin_sdl": "C:/Users/USERNAME/AppData/Roaming/djsoft.net/RadioBOSS_xxxxxxxxx/Presets/Schedule/Admin.sdl"
}
```

Danach starten

```bash
py scheduler.py
```

---

# 📅 Unterstützte RadioBOSS Daten

Der Scheduler verarbeitet derzeit

- Days
- Hours
- Minutes
- Seconds
- TimeType 1

Weitere Eventtypen werden in zukünftigen Versionen ergänzt.

---

# 🎯 Ziel des Projekts

Broadcast Scheduler soll kein Ersatz für RadioBOSS sein.

Das Ziel ist ein Werkzeug, mit dem man innerhalb weniger Sekunden erkennen kann:

- Welche Events laufen diese Woche?
- Gibt es Programmlücken?
- Gibt es Überschneidungen?
- Stimmen Moderationen?
- Stimmen News-Events?
- Ist das Programmschema korrekt?

---

# 🤝 Mitarbeit

Fehlerberichte und Verbesserungsvorschläge sind jederzeit willkommen.

---

# 📜 Lizenz

MIT License

---

# 👤 Autor

**Raymond Ummels**

Entwicklung mit Unterstützung von ChatGPT.

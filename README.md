# 📅 Broadcast Scheduler

![Version](https://img.shields.io/badge/version-2.3.0-blue)
![Python](https://img.shields.io/badge/Python-3.14-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

Broadcast Scheduler ist ein Analyse- und Planungswerkzeug für **RadioBOSS**.

Das Programm liest die originale **Admin.sdl** von RadioBOSS ein und erzeugt daraus einen übersichtlichen Wochen- oder Monatsplan. Dadurch lassen sich Sendeabläufe kontrollieren, Programmfehler erkennen und Sendeschemata überprüfen.

---

# 🖥 Screenshot

![Broadcast Scheduler](screenshot_01.PNG)

---

# ✨ Funktionen

## Bereits verfügbar

- ✅ Admin.sdl einlesen
- ✅ RadioBOSS Events analysieren
- ✅ Aktuelle Kalenderwoche automatisch erkennen
- ✅ Wochenplan erzeugen
- ✅ Sortierbare Tabelle
- ✅ Toolbar
- ✅ Vertikale und horizontale Scrollbars
- ✅ Statusleiste
- ✅ Mehrere Minuten pro Stunde (z.B. `17,43`)
- ✅ Unterstützung von `TimeType = 1`

---

# 🚧 Roadmap

## Version 2.4

- Gruppen anzeigen
- Detailfenster
- Toolbar erweitern
- Verbesserte Statusleiste
- Wochennavigation

## Version 2.5

- Monatsansicht
- Programmlücken erkennen
- Überschneidungen erkennen
- Konflikterkennung
- Suchfunktion

## Version 3.0

- PDF Export
- CSV Export
- Druckfunktion
- Farbige Eventtypen
- Erweiterte Filter
- Statistik

---

# 📂 Projektstruktur

```text
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
├── README.md
└── screenshot_01.PNG
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

Die Datei

```text
settings.example.json
```

nach

```text
settings.json
```

kopieren.

Anschließend den Pfad zur eigenen **Admin.sdl** eintragen.

Beispiel:

```json
{
    "admin_sdl": "C:/Users/USERNAME/AppData/Roaming/djsoft.net/RadioBOSS_xxxxxxxxx/Presets/Schedule/Admin.sdl"
}
```

Programm starten

```bash
py scheduler.py
```

---

# 📅 Unterstützte RadioBOSS Funktionen

Der Scheduler unterstützt derzeit:

- Days
- Hours
- Minutes
- Seconds
- TimeType 1

Weitere RadioBOSS-Funktionen werden schrittweise ergänzt.

---

# 🎯 Ziel des Projekts

Broadcast Scheduler ist **kein Ersatz für RadioBOSS**.

Das Ziel ist ein Analysewerkzeug, das innerhalb weniger Sekunden zeigt:

- Welche Events laufen diese Woche?
- Gibt es Programmlücken?
- Gibt es Überschneidungen?
- Stimmen Moderationen?
- Stimmen News-Events?
- Ist das Programmschema korrekt?

---

# 🤝 Mitarbeit

Verbesserungsvorschläge, Fehlerberichte und Pull Requests sind jederzeit willkommen.

---

# 📜 Lizenz

Dieses Projekt steht unter der **MIT License**.

Weitere Informationen siehe Datei **LICENSE**.

---

# 👤 Autor

**Raymond Ummels**

Entwicklung mit Unterstützung von ChatGPT.

---

⭐ Falls dir dieses Projekt gefällt, freue ich mich über einen **Star auf GitHub**.

# 📘 Broadcast Scheduler Installation Guide

This guide explains how to install and configure **Broadcast Scheduler for RadioBOSS**.

---

## Requirements

Before installing Broadcast Scheduler, make sure you have:

- Windows 10 or Windows 11
- Python 3.12 or newer
- RadioBOSS
- Tkinter, which is included with the standard Python installation

---

## 1. Download the Project

Clone the repository:

```bash
git clone https://github.com/mixnetwork1959/BroadcastScheduler.git
```

Alternatively, download the project as a ZIP file from GitHub and extract it to a folder of your choice.

---

## 2. Open the Project Folder

Open a command prompt in the project folder or use:

```bash
cd BroadcastScheduler
```

---

## 3. Create the Configuration File

Copy:

```text
settings.example.json
```

and rename the copy to:

```text
settings.json
```

Do not delete `settings.example.json`. It serves as the example configuration included with the project.

---

## 4. Find Your RadioBOSS Scheduler Profile

The easiest way to locate your scheduler profile is directly from RadioBOSS.

In RadioBOSS, open:

```text
Settings
→ Open Settings Folder
```

![Find the RadioBOSS settings folder](images/radioboss_find_SDL.PNG)

In the folder that opens, navigate to:

```text
Presets
→ Schedule
```

Inside the `Schedule` folder you will find one or more files with the `.sdl` extension.

Examples:

```text
Admin.sdl
Weekend.sdl
Studio.sdl
Production.sdl
MyRadio.sdl
```

Select the `.sdl` file that belongs to the RadioBOSS scheduler profile you want to analyze.

> The scheduler file is not always named `Admin.sdl`. Its name depends on the profile name used in RadioBOSS.

---

## 5. Configure `settings.json`

Open `settings.json` with a text editor and enter the full path to your own scheduler profile.

Example:

```json
{
  "admin_sdl": "C:/Users/USERNAME/AppData/Roaming/djsoft.net/RadioBOSS_xxxxxxxxx/Presets/Schedule/YourProfileName.sdl"
}
```

Replace:

- `USERNAME` with your Windows user name
- `RadioBOSS_xxxxxxxxx` with your actual RadioBOSS settings folder
- `YourProfileName.sdl` with the `.sdl` file you found in `Presets/Schedule`

Use forward slashes `/` in the JSON path, as shown in the example.

---

## 6. Start Broadcast Scheduler

Open a command prompt in the project folder and run:

```bash
py scheduler.py
```

The application will read the selected scheduler profile and display the current weekly schedule.

---

## Important

Broadcast Scheduler is a **read-only application**.

It:

- reads the selected `.sdl` file
- displays the scheduler events
- detects events that start at the same scheduled time
- never modifies your RadioBOSS scheduler
- never writes changes to the `.sdl` file

---

## Troubleshooting

### File not found

Check that the path in `settings.json` points to the correct `.sdl` file.

Also verify:

- the filename is correct
- the `.sdl` extension is included
- the RadioBOSS profile folder number is correct
- the JSON contains no extra braces or missing quotation marks

Correct example:

```json
{
  "admin_sdl": "C:/Path/To/YourProfileName.sdl"
}
```

### Python is not recognized

Install Python 3.12 or newer.

During installation, enable:

```text
Add Python to PATH
```

You can check the installed Python version with:

```bash
py --version
```

### Tkinter error

Tkinter is normally included with the standard Python installer for Windows.

If Tkinter is missing, reinstall Python using the standard Windows installer and make sure the optional Tcl/Tk components are enabled.

### No events are displayed

Check that:

- you selected the correct scheduler profile
- the events are enabled in RadioBOSS
- the scheduler uses currently supported scheduling options
- the selected week contains scheduled events

---

## Getting Help

When reporting a problem, please include:

- your Windows version
- your Python version
- your RadioBOSS version
- the complete error message
- the steps needed to reproduce the problem

Do not upload your private scheduler profile publicly unless you have checked that it contains no sensitive paths or information.

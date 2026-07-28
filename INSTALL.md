# INSTALL.md

# Broadcast Scheduler Installation Guide

## Requirements

-   Windows 10 or Windows 11
-   Python 3.12 or newer
-   RadioBOSS
-   Tkinter (included with Python)

## Installation

### 1. Download the project

Clone the repository:

``` bash
git clone https://github.com/mixnetwork1959/BroadcastScheduler.git
```

or download the ZIP file from GitHub.

### 2. Open the project folder

``` bash
cd BroadcastScheduler
```

### 3. Create your settings file

Copy:

    settings.example.json

to

    settings.json

### 4. Configure the Admin.sdl path

Example:

``` json
{
    "admin_sdl": "C:/Users/USERNAME/AppData/Roaming/djsoft.net/RadioBOSS_xxxxxxxxx/Presets/Schedule/Admin.sdl"
}
```

### 5. Start the application

``` bash
py scheduler.py
```

## Important

Broadcast Scheduler is **read-only**.

It never modifies your RadioBOSS schedule. It only reads the `Admin.sdl`
file.

## Troubleshooting

### File not found

Verify that the path in `settings.json` points to the correct
`Admin.sdl`.

### Python not found

Install Python 3.12+ and ensure it is added to the Windows PATH.

### Tkinter error

Tkinter is included with the standard Python installer.

# ❓ Frequently Asked Questions (FAQ)
4.5.0
# General

## What is Broadcast Scheduler?

Broadcast Scheduler is a companion application for RadioBOSS.

It helps you analyze, verify and publish your RadioBOSS scheduler.

The application is **not** a replacement for RadioBOSS.

---

## Does Broadcast Scheduler modify my RadioBOSS scheduler?

No.

Broadcast Scheduler is completely **read-only**.

It only reads your scheduler profile (`*.sdl`) and never writes changes back to RadioBOSS.

---

## Which RadioBOSS versions are supported?

Broadcast Scheduler has been developed and tested with RadioBOSS **7.2.2.0**.

Support for newer versions will be added when necessary.

---

# Scheduler

## Where is my scheduler profile located?

In RadioBOSS open:

```text
Settings
→ Open Settings Folder
→ Presets
→ Schedule
```

Your scheduler profile is stored as a `.sdl` file.

Examples:

```text
Admin.sdl
Studio.sdl
Weekend.sdl
MyRadio.sdl
```

The filename depends on the RadioBOSS profile you are using.

---

## Why do some events appear as conflicts?

A conflict simply means that two or more scheduler events are configured to start at exactly the same scheduled time.

This is not necessarily an error.

Some RadioBOSS configurations intentionally use simultaneous events.

---

## Why are some events not shown in the Public Calendar?

The Public Calendar is intended for listeners.

Technical scheduler events are intentionally excluded, for example:

- Time announcements
- Random jingles
- Weather updates
- Internal maintenance events

Only selected music programs should appear on the public website.

---

# Public Calendar

## What is the Public Calendar?

The Public Calendar creates a listener-friendly weekly schedule for your website.

It is completely independent from the RadioBOSS user interface.

---

## Can I rename programs?

Yes.

Each music program can have:

- Public name
- Description
- Color

without changing anything inside RadioBOSS.

---

## Can I hide programs?

Yes.

Simply disable the program inside the Public Calendar editor.

It will no longer appear on the generated website.

---

# Website Generator

## Do I need a web server?

No.

The generated HTML file is completely standalone.

Simply open it with your browser or upload it to your website.

---

## Does the generated website require PHP or a database?

No.

The website consists of a single HTML file.

No PHP.

No database.

No JavaScript framework.

---

## Does the website update automatically?

No.

Whenever your RadioBOSS schedule changes:

1. Open Broadcast Scheduler
2. Click **Publish Website**
3. Upload the new HTML file to your website

By default, the file is saved in:

```text
Documents/Broadcast Scheduler/Export/index.html
```

Use **Choose Export Folder** to select another location and
**Open Export Folder** to open it directly.

Future versions will support automatic FTP publishing.

---

# Troubleshooting

## No events are displayed

Please verify:

- the correct `.sdl` file is selected
- the scheduler contains enabled events
- the selected week contains scheduled events

---

## The website shows the wrong programs

Open the Public Calendar editor and verify that only your music programs are enabled.

---

## The generated website does not match RadioBOSS exactly

The Public Calendar is a simplified listener view.

Its purpose is to display your music schedule, not every internal RadioBOSS event.

---

# Support

If you find a bug or have a feature request, please open a GitHub Issue.

GitHub:

https://github.com/mixnetwork1959/BroadcastScheduler/issues

# ==========================================
# Broadcast Scheduler
# Version 2.7.0
# gui_calendar.py
# ==========================================

import tkinter as tk
from tkinter import ttk


LEFT = 70
TOP = 35

DAY_WIDTH = 210
HOUR_HEIGHT = 220

DAYS = (
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun"
)


# =====================================================
# Create Calendar
# =====================================================

def create_calendar(parent):

    frame = ttk.Frame(parent)

    frame.pack(
        fill="both",
        expand=True
    )

    vscroll = tk.Scrollbar(
        frame,
        orient="vertical"
    )

    vscroll.pack(
        side="right",
        fill="y"
    )

    hscroll = tk.Scrollbar(
        frame,
        orient="horizontal"
    )

    hscroll.pack(
        side="bottom",
        fill="x"
    )

    canvas = tk.Canvas(
        frame,
        bg="white",
        highlightthickness=0,
        yscrollcommand=vscroll.set,
        xscrollcommand=hscroll.set
    )

    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    vscroll.config(
        command=canvas.yview
    )

    hscroll.config(
        command=canvas.xview
    )

    return (
        frame,
        canvas,
        vscroll,
        hscroll
    )
# =====================================================
# Draw Header
# =====================================================

def draw_header(
    canvas,
    total_width
):

    for index, day in enumerate(DAYS):

        x = LEFT + (index * DAY_WIDTH)

        canvas.create_rectangle(
            x,
            0,
            x + DAY_WIDTH,
            TOP,
            fill="#ECECEC",
            outline="#C5C5C5"
        )

        canvas.create_text(
            x + DAY_WIDTH / 2,
            TOP / 2,
            text=day,
            font=("Segoe UI", 12, "bold")
        )
# =====================================================
# Draw Hours
# =====================================================

def draw_hours(
    canvas,
    total_width
):

    for hour in range(24):

        y = TOP + (hour * HOUR_HEIGHT)

        canvas.create_text(
            35,
            y + 10,
            text=f"{hour:02d}:00",
            font=("Segoe UI", 10, "bold")
        )

        canvas.create_line(
            LEFT,
            y,
            total_width,
            y,
            fill="#D9D9D9"
        )

    canvas.create_line(
        LEFT,
        TOP + (24 * HOUR_HEIGHT),
        total_width,
        TOP + (24 * HOUR_HEIGHT),
        fill="#D9D9D9"
    )
# =====================================================
# Draw Day Lines
# =====================================================

def draw_day_lines(
    canvas,
    total_height
):

    for day in range(8):

        x = LEFT + (day * DAY_WIDTH)

        canvas.create_line(
            x,
            TOP,
            x,
            total_height,
            fill="#CFCFCF"
        )
# =====================================================
# Draw Events
# =====================================================

def draw_events(
    canvas,
    runtimes
):

    if not runtimes:
        return

    week_start = runtimes[0].start.date()

    hour_events = {}

    for rt in runtimes:

        day = (
            rt.start.date() -
            week_start
        ).days

        if day < 0 or day > 6:
            continue

        key = (
            day,
            rt.start.hour
        )

        hour_events.setdefault(
            key,
            []
        ).append(rt)

    for (day, hour), events in hour_events.items():

        x = LEFT + (day * DAY_WIDTH) + 5
        y = TOP + (hour * HOUR_HEIGHT) + 5

        canvas.create_rectangle(
            x,
            y,
            x + DAY_WIDTH - 10,
            y + HOUR_HEIGHT - 10,
            fill="#F8F8F8",
            outline="#D0D0D0"
        )

        canvas.create_text(
            x + 6,
            y + 6,
            anchor="nw",
            text=f"{hour:02d}:00",
            font=("Segoe UI", 12, "bold")
        )

        yy = y + 28

        visible_events = 0

        for rt in events:

            group = rt.event.group.lower()

            if getattr(rt, "conflict", False):

                color = "#FFB3B3"
                outline = "#B00020"
                width = 2

            elif "music" in group:

                color = "#B7D7F7"
                outline = "#B8B8B8"
                width = 1

            elif "jingle" in group:

                color = "#BFE8BF"
                outline = "#B8B8B8"
                width = 1

            elif "news" in group:

                color = "#FFD699"
                outline = "#B8B8B8"
                width = 1

            elif "update" in group:

                color = "#FFF2A8"
                outline = "#B8B8B8"
                width = 1

            elif "moderation" in group:

                color = "#E6CCFF"
                outline = "#B8B8B8"
                width = 1

            else:

                color = "#EEEEEE"
                outline = "#B8B8B8"
                width = 1

            canvas.create_rectangle(
                x + 4,
                yy,
                x + DAY_WIDTH - 14,
                yy + 18,
                fill=color,
                outline=outline,
                width=width
            )

            canvas.create_text(
                x + 8,
                yy + 9,
                anchor="w",
                text=f"{rt.start:%H:%M}  {rt.event.name}",
                font=("Segoe UI", 10)
            )

            yy += 24

            visible_events += 1

            if yy > y + HOUR_HEIGHT - 20:

                hidden = (
                    len(events)
                    - visible_events
                )

                if hidden > 0:

                    canvas.create_text(
                        x + 8,
                        yy,
                        anchor="w",
                        text=f"(+{hidden})",
                        font=("Segoe UI", 8, "bold"),
                        fill="red"
                    )

                break
# =====================================================
# Draw Calendar
# =====================================================

def draw_calendar(
    canvas,
    runtimes
):
    """
    Draw the weekly calendar.
    """

    canvas.delete("all")

    total_width = LEFT + (len(DAYS) * DAY_WIDTH)
    total_height = TOP + (24 * HOUR_HEIGHT)

    canvas.configure(
        scrollregion=(
            0,
            0,
            total_width,
            total_height
        )
    )

    draw_header(
        canvas,
        total_width
    )

    draw_hours(
        canvas,
        total_width
    )

    draw_day_lines(
        canvas,
        total_height
    )

    draw_events(
        canvas,
        runtimes
    )                                
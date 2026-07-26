# ==========================================
# Broadcast Scheduler
# Version 2.5.1
# gui.py
#
# Part 1/3
# ==========================================

import tkinter as tk
from tkinter import ttk


# =====================================================
# Sort TreeView Column
# =====================================================

def sort_column(tree, column, reverse):

    data = [
        (tree.set(item, column), item)
        for item in tree.get_children("")
    ]

    data.sort(reverse=reverse)

    for index, (_, item) in enumerate(data):
        tree.move(item, "", index)

    tree.heading(
        column,
        command=lambda: sort_column(
            tree,
            column,
            not reverse
        )
    )
# =====================================================
# Populate TreeView
# =====================================================

def populate_tree(
    tree,
    runtimes,
    group="All",
    only_conflicts=False,
    search=""
):

    # Alte Einträge löschen
    tree.delete(*tree.get_children())

    for rt in runtimes:

        # ---------------------------------------------
        # Group Filter
        # ---------------------------------------------

        if group != "All":
            if rt.event.group != group:
                continue

               # ---------------------------------------------
        # Conflict Filter
        # ---------------------------------------------

        if only_conflicts:
            if not getattr(rt, "conflict", False):
                continue

          # ---------------------------------------------
        # Search Filter
        # ---------------------------------------------

        if search:

            text = (
                f"{rt.event.name} "
                f"{rt.event.group}"
            ).lower()

            if search.lower() not in text:
                continue

        # ---------------------------------------------
        # Status
        # ---------------------------------------------

        if getattr(rt, "conflict", False):
            status = "⚠ Please Check"
            tags = ("conflict",)
        else:
            status = "✓ OK"
            tags = ()

        values = (
            status,
            rt.start.strftime("%d.%m.%Y %H:%M:%S"),
            rt.event.group,
            rt.event.name
        )

        tree.insert(
            "",
            "end",
            values=values,
            tags=tags
        )
# =====================================================
# Draw Calendar
# =====================================================

def draw_calendar(canvas, runtimes):

    canvas.delete("all")

    LEFT = 70
    TOP = 35

    DAY_WIDTH = 210
    HOUR_HEIGHT = 220

    DAYS = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ]

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

    # -------------------------------------------------
    # Header
    # -------------------------------------------------

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

    # -------------------------------------------------
    # Hours
    # -------------------------------------------------

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

    # -------------------------------------------------
    # Day Lines
    # -------------------------------------------------

    for day in range(8):

        x = LEFT + (day * DAY_WIDTH)

        canvas.create_line(
            x,
            TOP,
            x,
            total_height,
            fill="#CFCFCF"
        )

    # -------------------------------------------------
    # Prepare Events
    # -------------------------------------------------

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

    # -------------------------------------------------
    # Draw Events
    # -------------------------------------------------
    for (day, hour), events in hour_events.items():

        x = LEFT + (day * DAY_WIDTH) + 5
        y = TOP + (hour * HOUR_HEIGHT) + 5

        # Stundenbox

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

            elif "music" in group:
                color = "#B7D7F7"

            elif "jingle" in group:
                color = "#BFE8BF"

            elif "news" in group:
                color = "#FFD699"

            elif "update" in group:
                color = "#FFF2A8"

            elif "moderation" in group:
                color = "#E6CCFF"

            else:
                color = "#EEEEEE"

            if getattr(rt, "conflict", False):
                outline = "#B00020"
                width = 2
            else:
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

                hidden = len(events) - visible_events

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
# Main Window
# =====================================================

def show_events(runtimes):

    root = tk.Tk()

    root.title("Broadcast Scheduler 2.5.1")
    root.geometry("1600x900")

    # =====================================================
    # Menu
    # =====================================================

    menubar = tk.Menu(root)

    file_menu = tk.Menu(
        menubar,
        tearoff=0
    )

    file_menu.add_command(
        label="Refresh"
    )

    file_menu.add_separator()

    file_menu.add_command(
        label="Exit",
        command=root.destroy
    )

    menubar.add_cascade(
        label="File",
        menu=file_menu
    )

    root.config(menu=menubar)

    # =====================================================
    # Toolbar
    # =====================================================

    toolbar = ttk.Frame(root)

    toolbar.pack(
        fill="x",
        padx=6,
        pady=6
    )

    ttk.Button(
        toolbar,
        text="🔄 Refresh"
    ).pack(
        side="left",
        padx=2
    )

    ttk.Button(
        toolbar,
        text="◀ Previous Week"
    ).pack(
        side="left",
        padx=2
    )

    ttk.Button(
        toolbar,
        text="Today"
    ).pack(
        side="left",
        padx=2
    )

    ttk.Button(
        toolbar,
        text="Next Week ▶"
    ).pack(
        side="left",
        padx=2
    )

    ttk.Button(
        toolbar,
        text="Month"
    ).pack(
        side="left",
        padx=2
    )
    # =====================================================
    # Search / Filter Bar
    # =====================================================

    filter_frame = ttk.Frame(root)

    filter_frame.pack(
        fill="x",
        padx=6,
        pady=(0, 6)
    )

    # -----------------------------------------------------
    # Search
    # -----------------------------------------------------

    ttk.Label(
        filter_frame,
        text="Search:"
    ).pack(
        side="left",
        padx=(0, 5)
    )

    search_var = tk.StringVar()

    search_entry = ttk.Entry(
        filter_frame,
        textvariable=search_var,
        width=35
    )

    search_entry.pack(
        side="left",
        padx=(0, 15)
    )

    # -----------------------------------------------------
    # Group
    # -----------------------------------------------------

    ttk.Label(
        filter_frame,
        text="Group:"
    ).pack(
        side="left",
        padx=(0, 5)
    )

    group_var = tk.StringVar(value="All")

    group_combo = ttk.Combobox(
        filter_frame,
        textvariable=group_var,
        values=["All"],
        state="readonly",
        width=20
    )

    group_combo.current(0)

    group_combo.pack(
        side="left",
        padx=(0, 15)
    )

    # -----------------------------------------------------
    # Only Conflicts
    # -----------------------------------------------------

    conflict_var = tk.BooleanVar(value=False)

    ttk.Checkbutton(
        filter_frame,
        text="Only Conflicts",
        variable=conflict_var
    ).pack(
        side="left"
    )

# =====================================================
# Notebook
# =====================================================

    notebook = ttk.Notebook(root)

    notebook.pack(
        fill="both",
        expand=True,
        padx=6,
        pady=6
    )

    # =====================================================
    # Events Tab
    # =====================================================

    events_tab = ttk.Frame(notebook)

    notebook.add(
        events_tab,
        text="Events"
    )

    # =====================================================
    # Calendar Tab
    # =====================================================

    calendar_tab = ttk.Frame(notebook)

    notebook.add(
        calendar_tab,
        text="Calendar"
    )

    # =====================================================
    # Calendar Frame
    # =====================================================

    calendar_frame = ttk.Frame(calendar_tab)

    calendar_frame.pack(
        fill="both",
        expand=True
    )

    # =====================================================
    # Calendar Scrollbars
    # =====================================================

    calendar_vscroll = tk.Scrollbar(
        calendar_frame,
        orient="vertical"
    )

    calendar_vscroll.pack(
        side="right",
        fill="y"
    )

    calendar_hscroll = tk.Scrollbar(
        calendar_frame,
        orient="horizontal"
    )

    calendar_hscroll.pack(
        side="bottom",
        fill="x"
    )

    # =====================================================
    # Calendar Canvas
    # =====================================================

    calendar_canvas = tk.Canvas(
        calendar_frame,
        bg="white",
        highlightthickness=0,
        yscrollcommand=calendar_vscroll.set,
        xscrollcommand=calendar_hscroll.set
    )

    calendar_canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    calendar_vscroll.config(
        command=calendar_canvas.yview
)

    calendar_hscroll.config(
        command=calendar_canvas.xview
)

    # =====================================================
    # Initial Draw
    # =====================================================

    def redraw_calendar(event=None):

        draw_calendar(
            calendar_canvas,
            runtimes
        )

    root.after(
        100,
        redraw_calendar
    )

    calendar_canvas.bind(
        "<Configure>",
        redraw_calendar
    )
        # Mouse Wheel

    calendar_canvas.bind(
        "<MouseWheel>",
        lambda e: calendar_canvas.yview_scroll(
            int(-1 * (e.delta / 120)),
            "units"
        )
    )

    # =====================================================
    # Main Frame
    # =====================================================

    frame = ttk.Frame(events_tab)

    frame.pack(
        fill="both",
        expand=True,
        padx=6,
        pady=6
    )

    # =====================================================
    # TreeView
    # =====================================================

    columns = (
        "Status",
        "Start",
        "Group",
        "Event"
    )

    tree = ttk.Treeview(
        frame,
        columns=columns,
        show="headings"
    )

    # =====================================================
    # Scrollbars
    # =====================================================

    vsb = tk.Scrollbar(
        frame,
        orient="vertical",
        command=tree.yview,
        width=20
    )

    hsb = tk.Scrollbar(
        frame,
        orient="horizontal",
        command=tree.xview,
        width=20
    )

    tree.configure(
        yscrollcommand=vsb.set,
        xscrollcommand=hsb.set
    )

    # =====================================================
    # Row Tags
    # =====================================================

    row_tags = {
        "conflict": "#FFF4CC",
    }

    for tag, color in row_tags.items():

        tree.tag_configure(
            tag,
            background=color
        )

    # =====================================================
    # Headings
    # =====================================================

    for column in columns:

        tree.heading(
            column,
            text=column,
            command=lambda c=column: sort_column(
                tree,
                c,
                False
            )
        )
    # =====================================================
    # Columns
    # =====================================================

    tree.column(
        "Status",
        width=90,
        anchor="center"
    )

    tree.column(
        "Start",
        width=190,
        anchor="center"
    )

    tree.column(
        "Group",
        width=220,
        anchor="w"
    )

    tree.column(
        "Event",
        width=820,
        anchor="w"
    )
    # =====================================================
    # Layout
    # =====================================================

    tree.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    vsb.grid(
        row=0,
        column=1,
        sticky="ns"
    )

    hsb.grid(
        row=1,
        column=0,
        sticky="ew"
    )

    frame.rowconfigure(
        0,
        weight=1
    )

    frame.columnconfigure(
        0,
        weight=1
    )
    # =====================================================
    # Prepare Group Filter
    # =====================================================

    groups = [
        "All",
        *sorted({
            rt.event.group
            for rt in runtimes
            if getattr(rt.event, "group", "")
        })
    ]

    group_combo.configure(values=groups)
    group_combo.current(0)

    # =====================================================
    # Populate TreeView
    # =====================================================

    def refresh_tree(event=None):
         populate_tree(
            tree,
            runtimes,
            group_var.get(),
            conflict_var.get(),
            search_var.get(),
        )

    group_combo.bind(
        "<<ComboboxSelected>>",
        refresh_tree
    )

    conflict_var.trace_add(
        "write",
        lambda *args: refresh_tree()
    )

    search_var.trace_add(
        "write",
        lambda *args: refresh_tree()
    )

    refresh_tree()
    # =====================================================
    # Status Bar
    # =====================================================

    event_count = len({rt.event.id for rt in runtimes})
    runtime_count = len(runtimes)

    conflict_count = sum(
        1
        for rt in runtimes
        if getattr(rt, "conflict", False)
    )

    ok_count = runtime_count - conflict_count

    if runtimes:
        week_start = runtimes[0].start.strftime("%d.%m.%Y")
        week_end = runtimes[-1].start.strftime("%d.%m.%Y")
    else:
        week_start = "-"
        week_end = "-"

    status = ttk.Label(
        root,
        text=(
            f"OK: {ok_count}    |    "
            f"Conflicts: {conflict_count}    |    "
            f"Events: {event_count}    |    "
            f"RunTimes: {runtime_count}    |    "
            f"Week: {week_start} - {week_end}"
        ),
        anchor="w",
        relief="sunken",
        padding=4
    )

    status.pack(
        fill="x",
        side="bottom"
    )

    # =====================================================
    # Start GUI
    # =====================================================

    root.mainloop()
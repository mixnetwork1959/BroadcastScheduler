# ==========================================
# Broadcast Scheduler
# Version 2.5.1
# gui.py
#
# Part 1/3
# ==========================================

import tkinter as tk
from tkinter import ttk
from gui_tree import (
    sort_column,
    populate_tree
)
from gui_statusbar import (
    create_statusbar,
    refresh_statusbar
)
from gui_filter import (
    create_filter_bar
)
from gui_toolbar import (
    create_toolbar
)
from gui_menu import (
    create_menu
)
from gui_treeview import (
    create_treeview
)
from gui_calendar import (
    create_calendar,
    draw_calendar
)

# =====================================================
# Main Window
# =====================================================

def show_events(controller, runtimes):

    root = tk.Tk()

    root.title("Broadcast Scheduler 2.5.1")
    root.geometry("1600x900")

        # =====================================================
    # Toolbar
    # =====================================================

    (
        toolbar,
        btn_refresh,
        btn_prev,
        btn_today,
        btn_next,
        btn_month
    ) = create_toolbar(root)

    (
        filter_frame,
        search_var,
        group_var,
        group_combo,
        conflict_var
    ) = create_filter_bar(root)

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
    # Calendar
    # =====================================================

    (
        calendar_frame,
        calendar_canvas,
        calendar_vscroll,
        calendar_hscroll
    ) = create_calendar(calendar_tab)

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
    # TreeView
    # =====================================================

    (
        frame,
        tree,
        columns,
        vsb,
        hsb
    ) = create_treeview(events_tab)

    # Sortierung aktivieren

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

    status = create_statusbar(root)

    refresh_statusbar(
        status,
        runtimes
    )

    # =====================================================
    # Start GUI
    # =====================================================

    root.mainloop()
# ==========================================
# Broadcast Scheduler
# Version 0.2.3
# gui.py
# ==========================================

import tkinter as tk
from tkinter import ttk

from parser import load_events


def show_events(filename, events, version):

    root = tk.Tk()
    root.title(f"Broadcast Scheduler v{version}")
    root.geometry("1100x700")

    active_only = tk.BooleanVar(value=False)
    search_text = tk.StringVar()

    columns = (
        "Name",
        "Aktiv",
        "Tage",
        "Zeit",
        "Minute"
    )

    toolbar = ttk.Frame(root, padding=5)
    toolbar.pack(fill="x")

    tree = ttk.Treeview(
        root,
        columns=columns,
        show="headings"
    )

    def fill_table():

        tree.delete(*tree.get_children())
        visible = 0
        active = 0

        search = search_text.get().lower().strip()

        for event in events:

            if active_only.get() and event["EnabledEvent"] != "1":
                continue

            if search and search not in event["TaskName"].lower():
                continue

            tage = " ".join(event["DayList"])

            if event["TimeBlocks"]:
                zeit = ", ".join(
                    f"{start} - {end}"
                    for start, end in event["TimeBlocks"]
                )
            else:
                zeit = "---"

            aktiv = "Ja" if event["EnabledEvent"] == "1" else "Nein"

            tree.insert(
                "",
                "end",
                values=(
                    event["TaskName"],
                    aktiv,
                    tage,
                    zeit,
                    event["Minutes"]
                )
            )

    def refresh():

        nonlocal events

        try:
            events = load_events(filename)
            fill_table()
        except Exception as e:
            print(e)

    chk = ttk.Checkbutton(
        toolbar,
        text="Nur aktive Events",
        variable=active_only,
        command=fill_table
    )

    chk.pack(side="left", padx=(0, 20))

    refresh_btn = ttk.Button(
        toolbar,
        text="🔄 Aktualisieren",
        command=refresh
    )

    refresh_btn.pack(side="left", padx=(0, 20))

    ttk.Label(
        toolbar,
        text="Suche:"
    ).pack(side="left")

    entry = ttk.Entry(
        toolbar,
        textvariable=search_text,
        width=35
    )

    entry.pack(side="left", padx=5)

    search_text.trace_add("write", lambda *args: fill_table())
    tree.heading("Name", text="Name")
    tree.heading("Aktiv", text="Aktiv")
    tree.heading("Tage", text="Tage")
    tree.heading("Zeit", text="Zeit")
    tree.heading("Minute", text="Minute")

    tree.column("Name", width=360)
    tree.column("Aktiv", width=70, anchor="center")
    tree.column("Tage", width=180)
    tree.column("Zeit", width=220)
    tree.column("Minute", width=80, anchor="center")
    tree.pack(fill="both", expand=True)

    status_var = tk.StringVar()

    status = ttk.Label(
        root,
        textvariable=status_var,
        anchor="w",
        relief="sunken",
        padding=(5, 2)
    )

    status.pack(fill="x", side="bottom")

    fill_table()

    root.mainloop()
# ==========================================
# Broadcast Scheduler
# Version 2.3.0
# gui.py
#
# Teil 1
# ==========================================

import tkinter as tk
from tkinter import ttk


# ---------------------------------------------------------
# Spalten sortieren
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# GUI
# ---------------------------------------------------------

def show_events(runtimes):

    root = tk.Tk()

    root.title("Broadcast Scheduler 2.3.0")
    root.geometry("1300x750")


    # =====================================================
    # Menü
    # =====================================================

    menubar = tk.Menu(root)

    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Aktualisieren")
    file_menu.add_separator()
    file_menu.add_command(label="Beenden", command=root.destroy)

    menubar.add_cascade(
        label="Datei",
        menu=file_menu
    )

    root.config(menu=menubar)


    # =====================================================
    # Toolbar
    # =====================================================

    toolbar = ttk.Frame(root)

    toolbar.pack(
        fill="x",
        padx=5,
        pady=5
    )

    ttk.Button(
        toolbar,
        text="🔄 Aktualisieren"
    ).pack(side="left", padx=2)

    ttk.Button(
        toolbar,
        text="◀ Woche"
    ).pack(side="left", padx=2)

    ttk.Button(
        toolbar,
        text="Heute"
    ).pack(side="left", padx=2)

    ttk.Button(
        toolbar,
        text="Woche ▶"
    ).pack(side="left", padx=2)

    ttk.Button(
        toolbar,
        text="Monat"
    ).pack(side="left", padx=2)


    # =====================================================
    # Hauptframe
    # =====================================================

    frame = ttk.Frame(root)

    frame.pack(
        fill="both",
        expand=True,
        padx=5,
        pady=5
    )
        # =====================================================
    # TreeView
    # =====================================================

    tree = ttk.Treeview(
        frame,
        columns=(
            "Start",
            "Ende",
            "Event"
        ),
        show="headings"
    )

    # -------------------------
    # Scrollbars
    # -------------------------

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

    # -------------------------
    # Spalten
    # -------------------------

    tree.heading(
        "Start",
        text="Start",
        command=lambda: sort_column(
            tree,
            "Start",
            False
        )
    )

    tree.heading(
        "Ende",
        text="Ende",
        command=lambda: sort_column(
            tree,
            "Ende",
            False
        )
    )

    tree.heading(
        "Event",
        text="Event",
        command=lambda: sort_column(
            tree,
            "Event",
            False
        )
    )

    tree.column(
        "Start",
        width=180,
        anchor="center"
    )

    tree.column(
        "Ende",
        width=180,
        anchor="center"
    )

    tree.column(
        "Event",
        width=750,
        anchor="w"
    )

    # -------------------------
    # Layout
    # -------------------------

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

    # -------------------------
    # Daten anzeigen
    # -------------------------

    for rt in runtimes:

        tree.insert(
            "",
            "end",
            values=(
                rt.start.strftime("%d.%m.%Y %H:%M:%S"),
                rt.end.strftime("%d.%m.%Y %H:%M:%S"),
                rt.event.name
            )
        )
            # =====================================================
    # Statusleiste
    # =====================================================

    status = ttk.Label(
        root,
        text=f"Events: {len(runtimes)}",
        anchor="w",
        relief="sunken"
    )

    status.pack(
        fill="x",
        side="bottom"
    )

    # =====================================================
    # Fenster anzeigen
    # =====================================================

    root.mainloop()
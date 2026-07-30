# ==========================================
# Broadcast Scheduler
# Version 4.4.0
# gui_menu.py
# ==========================================

import tkinter as tk


# =====================================================
# Create Menu
# =====================================================

def create_menu(
    root,
    refresh_command,
    theme_var,
    theme_command,
    themes
):

    menubar = tk.Menu(root)

    file_menu = tk.Menu(
        menubar,
        tearoff=0
    )

    file_menu.add_command(
    label="Refresh",
    command=refresh_command
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

    view_menu = tk.Menu(
        menubar,
        tearoff=0
    )

    theme_menu = tk.Menu(
        view_menu,
        tearoff=0
    )

    for theme_id, theme in themes.items():
        theme_menu.add_radiobutton(
            label=theme["name"],
            value=theme_id,
            variable=theme_var,
            command=theme_command
        )

    view_menu.add_cascade(
        label="Theme",
        menu=theme_menu
    )

    menubar.add_cascade(
        label="View",
        menu=view_menu
    )

    root.config(menu=menubar)

    return (
        menubar,
        file_menu,
        view_menu,
        theme_menu
    )

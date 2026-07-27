# ==========================================
# Broadcast Scheduler
# Version 2.7.0
# gui_menu.py
# ==========================================

import tkinter as tk


# =====================================================
# Create Menu
# =====================================================

def create_menu(root):

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

    return (
        menubar,
        file_menu
    )
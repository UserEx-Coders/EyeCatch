import tkinter as tk

BG = "#0F1115"
SURFACE = "#171A21"

PRIMARY = "#00E5FF"

TEXT = "#FFFFFF"
MUTED = "#8B93A7"


class Sidebar(tk.Frame):

    def __init__(self, parent, navigate):

        super().__init__(
            parent,
            bg=BG,
            width=240
        )

        self.pack_propagate(False)

        tk.Label(
            self,
            text="USEREX",
            bg=BG,
            fg=PRIMARY,
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=24,
            pady=(30, 0)
        )

        tk.Label(
            self,
            text="System Tracker",
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            padx=24,
            pady=(0, 30)
        )

        items = [
            ("CPU", "cpu"),
            ("Memory", "ram"),
            ("Disk", "disk"),
            ("Network", "network"),
            ("Processes", "process")
        ]

        for text, route in items:

            tk.Button(
                self,
                text=text,
                command=lambda r=route: navigate(r),
                bg=SURFACE,
                fg=TEXT,
                relief="flat",
                bd=0,
                padx=20,
                pady=14,
                anchor="w",
                cursor="hand2",
                font=("Segoe UI", 11)
            ).pack(
                fill="x",
                padx=15,
                pady=5
            )
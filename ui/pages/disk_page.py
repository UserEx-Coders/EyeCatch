import tkinter as tk

from ui.components.metric_card import MetricCard

class DiskPage:
        
    def __init__(self, parent, data):

        self.parent = parent
        self.data = data

        self.usage_var = tk.StringVar()
        self.total_var = tk.StringVar()
        self.free_var = tk.StringVar()
        self.read_var = tk.StringVar()
        self.write_var = tk.StringVar()

    def render(self):

        tk.Label(
            self.parent,
            text="Disk Overview",
            bg="#0F1115",
            fg="#FFFFFF",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )

        grid = tk.Frame(
            self.parent,
            bg="#0F1115"
        )

        grid.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        grid.columnconfigure(0, weight=1, uniform="cards")
        grid.columnconfigure(1, weight=1, uniform="cards")

        grid.rowconfigure(0, weight=1)
        grid.rowconfigure(1, weight=1)
        grid.rowconfigure(2, weight=1)

        usage_card = MetricCard(
            grid,
            "Usage",
            self.usage_var
        )

        usage_card.grid(
            row=0,
            column=0,
            padx=12,
            pady=12,
            sticky="nsew"
        )

        total_card = MetricCard(
            grid,
            "Total",
            self.total_var
        )

        total_card.grid(
            row=0,
            column=1,
            padx=12,
            pady=12,
            sticky="nsew"
        )

        free_card = MetricCard(
            grid,
            "Free",
            self.free_var
        )

        free_card.grid(
            row=1,
            column=0,
            padx=12,
            pady=12,
            sticky="nsew"
        )

        read_card = MetricCard(
            grid,
            "Read Speed",
            self.read_var
        )

        read_card.grid(
            row=1,
            column=1,
            padx=12,
            pady=12,
            sticky="nsew"
        )

        write_card = MetricCard(
            grid,
            "Write Speed",
            self.write_var
        )

        write_card.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=12,
            pady=12,
            sticky="nsew"
        )

        self.update(self.data)

    def update(self, data):

        if not data:
            return

        self.usage_var.set(
            f"{data.usage:.1f}%"
        )

        self.total_var.set(
            f"{data.total:.2f} GB"
        )

        self.free_var.set(
            f"{data.free:.2f} GB"
        )

        self.read_var.set(
            f"{data.read_speed:.2f} MB/s"
        )

        self.write_var.set(
            f"{data.write_speed:.2f} MB/s"
        )

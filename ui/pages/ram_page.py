import tkinter as tk

from ui.components.metric_card import MetricCard

class RAMPage:

    def __init__(self, parent, data):

        self.parent = parent
        self.data = data

        self.total_var = tk.StringVar()
        self.used_var = tk.StringVar()
        self.available_var = tk.StringVar()
        self.percent_var = tk.StringVar()

    def render(self):

        tk.Label(
            self.parent,
            text="Memory Overview",
            bg="#0F1115",
            fg="#FFFFFF",
            font=("Segoe UI", 24, "bold")
        ).pack(anchor="w", padx=25, pady=(20, 15))

        grid = tk.Frame(self.parent, bg="#0F1115")
        grid.pack(fill="both", expand=True, padx=15)

        grid.columnconfigure(0, weight=1, uniform="cards")
        grid.columnconfigure(1, weight=1, uniform="cards")

        MetricCard(grid, "Usage", self.percent_var)\
            .grid(row=0, column=0, padx=12, pady=12, sticky="nsew")

        MetricCard(grid, "Used", self.used_var)\
            .grid(row=0, column=1, padx=12, pady=12, sticky="nsew")

        MetricCard(grid, "Available", self.available_var)\
            .grid(row=1, column=0, padx=12, pady=12, sticky="nsew")

        MetricCard(grid, "Total", self.total_var)\
            .grid(row=1, column=1, padx=12, pady=12, sticky="nsew")

        self.update(self.data)

    def update(self, data):

        if not data:
            return

        self.percent_var.set(f"{data.percent:.1f}%")
        self.used_var.set(f"{data.used:.2f} GB")
        self.available_var.set(f"{data.available:.2f} GB")
        self.total_var.set(f"{data.total:.2f} GB")
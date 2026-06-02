import tkinter as tk

from ui.components.metric_card import MetricCard

class CPUPage:

    def __init__(self, parent, data):

        self.parent = parent
        self.data = data

        self.usage_var = tk.StringVar()
        self.temp_var = tk.StringVar()
        self.freq_var = tk.StringVar()
        self.cores_var = tk.StringVar()
        self.threads_var = tk.StringVar()

    def render(self):

        tk.Label(
            self.parent,
            text="CPU Overview",
            bg="#0F1115",
            fg="#FFFFFF",
            font=("Segoe UI", 24, "bold")
        ).pack(anchor="w", padx=25, pady=(20, 15))

        grid = tk.Frame(self.parent, bg="#0F1115")
        grid.pack(fill="both", expand=True, padx=15)

        grid.columnconfigure(0, weight=1, uniform="cards")
        grid.columnconfigure(1, weight=1, uniform="cards")

        MetricCard(grid, "Usage", self.usage_var)\
            .grid(row=0, column=0, padx=12, pady=12, sticky="nsew")

        MetricCard(grid, "Temperature", self.temp_var)\
            .grid(row=0, column=1, padx=12, pady=12, sticky="nsew")

        MetricCard(grid, "Frequency", self.freq_var)\
            .grid(row=1, column=0, padx=12, pady=12, sticky="nsew")

        MetricCard(grid, "Cores", self.cores_var)\
            .grid(row=1, column=1, padx=12, pady=12, sticky="nsew")

        MetricCard(grid, "Threads", self.threads_var)\
            .grid(row=2, column=0, columnspan=2, padx=12, pady=12, sticky="nsew")

        self.update(self.data)

    def update(self, data):

        if not data:
            return

        self.usage_var.set(f"{data.usage:.1f}%")
        self.temp_var.set(data.temperature)
        self.freq_var.set(data.frequency)
        self.cores_var.set(str(data.cores))
        self.threads_var.set(str(data.threads))
import tkinter as tk

from ui.components.metric_card import MetricCard

class NetworkPage:

    def __init__(self, parent, data):

        self.parent = parent
        self.data = data

        self.upload_var = tk.StringVar()
        self.download_var = tk.StringVar()
        self.sent_var = tk.StringVar()
        self.recv_var = tk.StringVar()

    def render(self):

        tk.Label(
            self.parent,
            text="Network Overview",
            bg="#0F1115",
            fg="#FFFFFF",
            font=("Segoe UI", 24, "bold")
        ).pack(anchor="w", padx=25, pady=(20, 15))

        grid = tk.Frame(self.parent, bg="#0F1115")
        grid.pack(fill="both", expand=True, padx=15)

        grid.columnconfigure(0, weight=1, uniform="cards")
        grid.columnconfigure(1, weight=1, uniform="cards")

        MetricCard(grid, "Upload", self.upload_var)\
            .grid(row=0, column=0, padx=12, pady=12, sticky="nsew")

        MetricCard(grid, "Download", self.download_var)\
            .grid(row=0, column=1, padx=12, pady=12, sticky="nsew")

        MetricCard(grid, "Total Sent", self.sent_var)\
            .grid(row=1, column=0, padx=12, pady=12, sticky="nsew")

        MetricCard(grid, "Total Received", self.recv_var)\
            .grid(row=1, column=1, padx=12, pady=12, sticky="nsew")

        self.update(self.data)

    def update(self, data):

        if not data:
            return

        self.upload_var.set(
            f"{data.sent_speed:.2f} KB/s"
        )

        self.download_var.set(
            f"{data.received_speed:.2f} KB/s"
        )

        self.sent_var.set(
            f"{data.total_sent / (1024**2):.2f} MB"
        )

        self.recv_var.set(
            f"{data.total_received / (1024**2):.2f} MB"
        )
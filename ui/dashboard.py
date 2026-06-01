import tkinter as tk
from tkinter import ttk
from core.monitor import SystemMonitor

class DashboardApp:
    def __init__(self, root: tk.Tk, monitor: SystemMonitor):
        self.root = root
        self.monitor = monitor

        self.root.title("UserEx Monitor")
        self.root.geometry("420x280")
        self.root.resizable(False, False)

        self.usage_var = tk.StringVar(value="--")
        self.temperature_var = tk.StringVar(value="--")
        self.frequency_var = tk.StringVar(value="--")
        self.cores_var = tk.StringVar(value="--")
        self.threads_var = tk.StringVar(value="--")

        self._build_ui()
        self.update_cpu()

    def _build_ui(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        title = ttk.Label(main_frame, text="CPU", font=("Segoe UI", 20, "bold"))
        title.pack(anchor="w", pady=(0, 15))

        card = ttk.Frame(main_frame, padding=15, relief="ridge")
        card.pack(fill="both", expand=True)

        self._add_row(card, "Uso", self.usage_var, 0)
        self._add_row(card, "Temperatura", self.temperature_var, 1)
        self._add_row(card, "Frequência", self.frequency_var, 2)
        self._add_row(card, "Núcleos", self.cores_var, 3)
        self._add_row(card, "Threads", self.threads_var, 4)

    def _add_row(self, parent, label_text, variable, row):
        label = ttk.Label(parent, text=label_text + ":")
        label.grid(row=row, column=0, sticky="w", padx=(0, 20), pady=6)

        value = ttk.Label(parent, textvariable=variable, font=("Segoe UI", 10, "bold"))
        value.grid(row=row, column=1, sticky="w", pady=6)

    def update_cpu(self):
        info = self.monitor.get_cpu_info()

        self.usage_var.set(f"{info.usage:.1f}%")
        self.temperature_var.set(info.temperature)
        self.frequency_var.set(info.frequency)
        self.cores_var.set(str(info.cores))
        self.threads_var.set(str(info.threads))

        self.root.after(250, self.update_cpu)
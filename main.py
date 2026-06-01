import tkinter as tk
from core.monitor import SystemMonitor
from ui.dashboard import DashboardApp

def main():
    root = tk.Tk()
    monitor = SystemMonitor()

    cpu = monitor.get_cpu_info()
    ram = monitor.get_ram_info()
    disk = monitor.get_disk_info()

    app = DashboardApp(root, monitor)
    root.mainloop()

if __name__ == "__main__":
    main()
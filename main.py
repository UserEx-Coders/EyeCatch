import tkinter as tk
from core.monitor import SystemMonitor
from ui.dashboard import DashboardApp

def main():
    root = tk.Tk()
    monitor = SystemMonitor()
    app = DashboardApp(root, monitor)
    root.mainloop()

if __name__ == "__main__":
    main()
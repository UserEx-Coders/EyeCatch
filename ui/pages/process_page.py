import tkinter as tk
from tkinter import ttk

class ProcessPage:

    def __init__(self, parent, data):

        self.parent = parent
        self.data = data or []

        self.tree = None
        self.rows = []

    def render(self):

        tk.Label(
            self.parent,
            text="Processes",
            bg="#0F1115",
            fg="#FFFFFF",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )

        container = tk.Frame(
            self.parent,
            bg="#0F1115"
        )

        container.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(0, 20)
        )

        self.tree = ttk.Treeview(
            container,
            columns=(
                "pid",
                "name",
                "cpu",
                "memory",
                "status"
            ),
            show="headings"
        )

        self.tree.heading("pid", text="PID")
        self.tree.heading("name", text="Process")
        self.tree.heading("cpu", text="CPU %")
        self.tree.heading("memory", text="Memory %")
        self.tree.heading("status", text="Status")

        self.tree.column("pid", width=70, anchor="center")
        self.tree.column("name", width=260)
        self.tree.column("cpu", width=90, anchor="center")
        self.tree.column("memory", width=100, anchor="center")
        self.tree.column("status", width=120, anchor="center")

        self.tree.pack(
            fill="both",
            expand=True
        )

        self.update(self.data)

    def update(self, data):

        if not data:
            return

        if self.tree is None:
            return

        while len(self.rows) < len(data):

            iid = self.tree.insert(
                "",
                "end",
                values=("", "", "", "", "")
            )

            self.rows.append(iid)

        for i, proc in enumerate(data):

            self.tree.item(
                self.rows[i],
                values=(
                    proc.pid,
                    proc.name,
                    f"{proc.cpu:.1f}",
                    f"{proc.memory:.1f}",
                    proc.status
                )
            )
import tkinter as tk


class MetricCard(tk.Frame):

    def __init__(self, parent, title, variable):

        super().__init__(
            parent,
            bg="#171A21",
            width=320,
            height=160,
            highlightthickness=1,
            highlightbackground="#252A35"
        )

        self.grid_propagate(False)

        tk.Label(
            self,
            text=title,
            bg="#171A21",
            fg="#9CA3AF",
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 0)
        )

        tk.Label(
            self,
            textvariable=variable,
            bg="#171A21",
            fg="#FFFFFF",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(12, 0)
        )
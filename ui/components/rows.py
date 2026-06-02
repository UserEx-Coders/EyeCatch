from tkinter import ttk


def add_row(parent, label_text, variable, row):

    label = ttk.Label(
        parent,
        text=label_text
    )

    value = ttk.Label(
        parent,
        textvariable=variable
    )

    label.grid(
        row=row,
        column=0,
        sticky="w",
        padx=(0, 20),
        pady=8
    )

    value.grid(
        row=row,
        column=1,
        sticky="e",
        pady=8
    )
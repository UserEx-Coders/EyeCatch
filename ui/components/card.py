import tkinter as tk
from ui.theme.tokens import CARD, BORDER


class Card(tk.Frame):

    def __init__(self, parent):
        super().__init__(
            parent,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER
        )
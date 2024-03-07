import tkinter as tk
import random

class Memorama:
    def _init_(self, master, rows=4, columns=4):
        self.master = master
        self.rows = rows
        self.columns = columns
        self.cards = [i for i in range(1, (rows * columns) // 2 + 1)] * 2
        random.shuffle(self.cards)
        self.buttons = []
        self.first_card = None
        self.second_card = None
        self.create_widgets()
    def create_widgets(self):
        for i, card in enumerate(self.cards):
            row, col = divmod(i, self.columns)
            button = tk.Button(self.master, text=" ", width=6, height=3,
                               command=lambda row=row, col=col: self.on_click(row, col))
            button.grid(row=row, column=col)
            self.buttons.append(button)
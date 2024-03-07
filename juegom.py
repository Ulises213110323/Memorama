import tkinter as tk
import random

class Memorama:
    def init(self, master, rows=4, columns=4):
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

    def on_click(self, row, col):
        index = row * self.columns + col
        card = self.cards[index]
        self.show_card(row, col, card)
        if self.first_card is None:
            self.first_card = (row, col, card)
        else:
            self.second_card = (row, col, card)
            if self.first_card[2] == self.second_card[2]:
                self.first_card = None
                self.second_card = None
            else:
                self.master.after(1000, self.hide_cards)

    def show_card(self, row, col, card):
        index = row * self.columns + col
        self.buttons[index].config(text=str(card))
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

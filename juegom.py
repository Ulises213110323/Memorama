import tkinter as tk
import random
import time

class Memorama:
    def __init__(self, master, rows=4, columns=4):
        self.master = master
        self.rows = rows
        self.columns = columns
        # Generar las cartas y mezclarlas
        self.cards = [i for i in range(1, (rows * columns) // 2 + 1)] * 2
        random.shuffle(self.cards)
        self.buttons = []  # Lista para almacenar los botones
        self.first_card = None
        self.second_card = None
        self.create_widgets()  # Crear la interfaz gráfica del juego

    def create_widgets(self):
        # Crear botones para cada carta en el tablero
        for i in range(self.rows):
            for j in range(self.columns):
                # Cada botón llama a la función on_click con su posición
                button = tk.Button(self.master, text=" ", width=6, height=3,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)  # Colocar el botón en la ventana
                self.buttons.append(button)  # Agregar el botón a la lista

    def on_click(self, row, col):
        index = row * self.columns + col
        card = self.cards[index]
        self.show_card(row, col, card)  # Mostrar la carta cuando se hace clic
        if self.first_card is None:
            self.first_card = (row, col, card)
        else:
            self.second_card = (row, col, card)
            if self.first_card[2] == self.second_card[2]:
                self.first_card = None
                self.second_card = None
            else:
                self.master.after(1000, self.hide_cards)  # Ocultar las cartas después de un tiempo

    def show_card(self, row, col, card):
        index = row * self.columns + col
        self.buttons[index].config(text=str(card))  # Mostrar el texto de la carta en el botón

    def hide_cards(self):
        # Ocultar las cartas después de un tiempo
        row1, col1, _ = self.first_card
        row2, col2, _ = self.second_card
        index1 = row1 * self.columns + col1
        index2 = row2 * self.columns + col2
        self.buttons[index1].config(text=" ")  # Ocultar la primera carta
        self.buttons[index2].config(text=" ")  # Ocultar la segunda carta
        self.first_card = None
        self.second_card = None

def main():
    root = tk.Tk()
    root.title("Memorama")
    game = Memorama(root)
    root.mainloop()

if __name__ == "__main__":
    main()

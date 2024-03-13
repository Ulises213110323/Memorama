import tkinter as tk
import random

class Memorama:
    def __init__(self, master, rows=4, columns=4):
        self.master = master
        self.rows = rows
        self.columns = columns
        # Creamos una lista con las cartas, cada número representa una carta
        self.cards = [i for i in range(1, (rows * columns) // 2 + 1)] * 2
        random.shuffle(self.cards)  # Mezclamos las cartas
        self.buttons = []  # Lista para almacenar los botones de las cartas
        self.first_card = None  # Almacena la primera carta seleccionada
        self.second_card = None  # Almacena la segunda carta seleccionada
        self.create_widgets()  # Método para crear los botones de las cartas
    
    def __repr__(self):
        return f'Memorama(rows={self.rows}, columns={self.columns})'

    def create_widgets(self):
        # Creamos los botones para las cartas y los añadimos a la lista de botones
        for i in range(self.rows):
            for j in range(self.columns):
                button = tk.Button(self.master, text=" ", width=6, height=3,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j, sticky="nsew")  # Añadimos los botones al grid
                self.buttons.append(button)

    def on_click(self, row, col):
        index = row * self.columns + col  # Convertimos la posición del botón a un índice de la lista de cartas
        card = self.cards[index]  # Obtenemos el número de la carta
        self.show_card(row, col, card)  # Mostramos la carta en el botón
        if self.first_card is None:  # Si es la primera carta seleccionada
            self.first_card = (row, col, card)
        else:
            self.second_card = (row, col, card)  # Si es la segunda carta seleccionada
            if self.first_card[2] == self.second_card[2]:  # Si las cartas son iguales
                self.first_card = None
                self.second_card = None
            else:
                self.master.after(1000, self.hide_cards)  # Si las cartas no son iguales, las ocultamos después de 1 segundo

    def show_card(self, row, col, card):
        index = row * self.columns + col
        self.buttons[index].config(text=str(card))  # Mostramos el número de la carta en el botón

    def hide_cards(self):
        row1, col1, _ = self.first_card
        row2, col2, _ = self.second_card
        index1 = row1 * self.columns + col1
        index2 = row2 * self.columns + col2
        self.buttons[index1].config(text=" ")  # Ocultamos la primera carta
        self.buttons[index2].config(text=" ")  # Ocultamos la segunda carta
        self.first_card = None
        self.second_card = None

def main():
    root = tk.Tk()
    root.title("Memorama")
    game = Memorama(root)
    root.mainloop()

if __name__ == "__main__":
    main()

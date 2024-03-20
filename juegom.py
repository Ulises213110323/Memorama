import tkinter as tk  # Importar la biblioteca tkinter para la interfaz gráfica
import random  # Importar la biblioteca random para generar números aleatorios
import threading  # Importar threading para ejecutar operaciones en segundo plano
import requests  # Importar la biblioteca requests para realizar solicitudes HTTP
import json  # Importar la biblioteca json para manejar datos en formato JSON
import openai  # Importar la biblioteca OpenAI para interactuar con la API de OpenAI

# Establecer la URL base de la API de OpenAI y la clave de la API
openai.api_base = "https://api.openai.com/v1/chat/completions" 
openai.api_key = "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"

class Memorama:
    def __init__(self, master, rows=4, columns=4):
        self.master = master  # Guardar la referencia al widget principal
        self.rows = rows  # Número de filas del tablero del juego
        self.columns = columns  # Número de columnas del tablero del juego
        # Generar las cartas y mezclarlas
        self.cards = [i for i in range(1, (rows * columns) // 2 + 1)] * 2
        random.shuffle(self.cards)
        self.buttons = []  # Lista para almacenar los botones del tablero
        self.first_card = None  # Almacenar la primera carta seleccionada por el jugador
        self.second_card = None  # Almacenar la segunda carta seleccionada por el jugador
        self.create_widgets()  # Crear la interfaz gráfica del juego

    def create_widgets(self):
        # Crear botones para cada carta en el tablero
        for i in range(self.rows):
            for j in range(self.columns):
                button = tk.Button(self.master, text=" ", width=6, height=3,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)  # Colocar el botón en la ventana
                self.buttons.append(button)  # Agregar el botón a la lista de botones

    def on_click(self, row, col):
        index = row * self.columns + col
        card = self.cards[index]  # Obtener el número de la carta seleccionada
        self.show_card(row, col, card)  # Mostrar la carta seleccionada en el tablero
        if self.first_card is None:
            self.first_card = (row, col, card)  # Almacenar la primera carta seleccionada
        else:
            self.second_card = (row, col, card)  # Almacenar la segunda carta seleccionada
            if self.first_card[2] == self.second_card[2]:  # Verificar si las cartas son iguales
                self.first_card = None  # Reiniciar la selección de cartas
                self.second_card = None
                self.show_motivational_message(ganador=True)  # Mostrar mensaje motivacional si el jugador gana
            else:
                self.master.after(1000, self.hide_cards)  # Ocultar las cartas después de un tiempo

    def show_card(self, row, col, card):
        index = row * self.columns + col
        self.buttons[index].config(text=str(card))  # Mostrar el número de la carta en el botón correspondiente

    def hide_cards(self):
        if self.first_card is not None:
            row1, col1, _ = self.first_card
            row2, col2, _ = self.second_card
            index1 = row1 * self.columns + col1
            index2 = row2 * self.columns + col2
            self.buttons[index1].config(text=" ")  # Ocultar la primera carta
            self.buttons[index2].config(text=" ")  # Ocultar la segunda carta
            self.first_card = None  # Reiniciar la selección de cartas
            self.second_card = None

    def show_motivational_message(self, ganador):
        threading.Thread(target=self._generar_mensaje_motivacional, args=(ganador,)).start()

    def _generar_mensaje_motivacional(self, ganador):
        prompt = "Tu " + ("ganaste" if ganador else "perdiste") + " el juego. Genera un mensaje motivacional."
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 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"  
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.5,
            "max_tokens": 50
        }
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        motivational_message = response_data["choices"][0]["message"]["content"].strip()
        print("Mensaje motivacional:", motivational_message)

def main():
    root = tk.Tk()
    root.title("Memorama")
    game = Memorama(root)
    root.mainloop()

if __name__== "__main__":
    main()

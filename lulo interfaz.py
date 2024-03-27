import tkinter as tk
from datetime import datetime as dt
from tkinter import simpledialog
import lulo_dinero as ld 
import capitales2 as cp
import lulo_chiste as lch

class ChatbotInterfaz:
    def __init__(self, master):
        self.master = master
        master.title("Lulo Chatbot")

        self.chat_log = tk.Text(master, state=tk.DISABLED, width=40, height=20)
        self.chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.input_field = tk.Entry(master, width=30)
        self.input_field.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(master, text="Enviar", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

    def send_message(self):
        message = self.input_field.get()
        self.input_field.delete(0, tk.END)
        self.display_message("Tú: " + message)
        self.process_message(message)

    def display_message(self, message):
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.config(state=tk.DISABLED)
        self.chat_log.see(tk.END)

    def process_message(self, message):
        if message == "cuál es tu edad?":
            self.display_message("Soy una IA, no tengo edad.")
        elif message.startswith("Hola") or (message.startswith("hola")):
            self.display_message("¡Hola! ¿Cómo estás?")
        elif message == "de donde eres?":
            self.display_message("Soy de Colombia.")
        elif message == "que dia es hoy?":
            self.display_message("Hoy es " + str(dt.now()))
        elif message == "cual es tu comida favorita?":
            self.display_message("Me encanta la pasta. ¿Y a ti?")
        elif message == "cual es el pais mas grande del mundo ?":
            self.display_message("El país más grande del mundo es Rusia.")
        elif message == "cual es el animal mas rapido del mundo ?":
            self.display_message("El animal más rápido del mundo es el guepardo.")
        elif "nombre" in message or "llamas" in message:
            self.display_message("Me llamo Lulo.")
        elif "capital" in message:
            pais = simpledialog.askstring("País", "¿De qué país deseas saber la capital?")
            if pais:
                self.display_message(cp.obtenercapital(pais))
            else:
                self.display_message("Por favor ingresa un nombre de país.")
        elif "chiste" in message:
            self.display_message(lch.lulo_chistes())
        elif "dolar" in message or "peso" in message:
            respuesta2 = input("Escoge una opción (1) de peso a dolar (2) de dolar a peso: ")
            if respuesta2 == "1" or respuesta2 == "2":
                cantidad = float(input("Ingresa la cantidad a convertir: "))
                if respuesta2 == "1":
                    self.display_message(ld.peso_dolar(cantidad))
                else:
                    self.display_message(ld.dolar_a_peso(cantidad))
            else:
                self.display_message("Opción no válida. Por favor selecciona 1 o 2.")
        else:
            self.display_message("Lo siento, no entendí. ¿Puedes repetirlo o preguntar de otra manera?")

def main():
    root = tk.Tk()
    chatbot_interfaz = ChatbotInterfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()

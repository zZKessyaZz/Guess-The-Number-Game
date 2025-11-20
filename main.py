import tkinter as tk
import random

janela = tk.Tk()
janela.title("Guess The Number Game")
janela.geometry("500x400")
janela.configure(bg="gray")

titulo = tk.Label(janela, text="Adivinhe o Número (1 a 100)", font=("Arial",14,"bold"), bg = "gray")
titulo.pack(pady = 20)



janela.mainloop()
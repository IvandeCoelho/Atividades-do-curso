from tkinter import *
from tkinter import ttk
from time import sleep
from threading import Thread

def atualizar_progressbar(progressbar, max_value=100, delay=0.3):
    """
    Atualiza a barra de progresso em uma thread separada.
    :param progressbar: Progressbar a ser atualizada.
    :param max_value: Valor máximo da barra de progresso.
    :param delay: Intervalo entre as atualizações (em segundos).
    """
    def atualizar():
        for x in range(max_value + 1):
            progressbar["value"] = x
            progressbar.update_idletasks()
            sleep(delay)
    Thread(target=atualizar).start()

# Janela principal
root = Tk()
root.geometry("300x200")

# Frame principal
frame = Frame(root)
frame.pack(pady=20)

# Barra de progresso
progressbar = ttk.Progressbar(frame, orient=HORIZONTAL, length=200, mode="determinate")
progressbar.pack(pady=5)

# Botão para iniciar a progressão
botao = ttk.Button(frame, text="Iniciar", command=lambda: atualizar_progressbar(progressbar))
botao.pack(pady=10)

root.mainloop()

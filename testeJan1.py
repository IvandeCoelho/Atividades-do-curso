from tkinter import *
from tkinter import ttk

def criar_janela_ttk():
    janela = Tk()
    janela.title("Widgets TTK")
    janela.geometry("500x500")

    # Estilo personalizado para melhorar a aparência
    estilo = ttk.Style()
    estilo.theme_use("default")
    estilo.configure("TLabel", font=("Arial", 12), padding=5)
    estilo.configure("TButton", font=("Arial", 12), padding=5)
    estilo.configure("TEntry", font=("Arial", 12), padding=5)
    estilo.configure("TCombobox", font=("Arial", 12), padding=5)

    # Label
    ttk.Label(janela, text="Este é um Label").pack(pady=5)

    # Entry
    ttk.Entry(janela).pack(pady=5)

    # Button
    ttk.Button(janela, text="Clique Aqui").pack(pady=5)

    # Combobox
    ttk.Combobox(janela, values=["Opção 1", "Opção 2", "Opção 3"]).pack(pady=5)

    # Checkbutton
    check_var = BooleanVar()
    ttk.Checkbutton(janela, text="Marque-me", variable=check_var).pack(pady=5)

    # Radiobutton
    radio_var = StringVar(value="1")
    ttk.Radiobutton(janela, text="Opção 1", value="1", variable=radio_var).pack(pady=5)
    ttk.Radiobutton(janela, text="Opção 2", value="2", variable=radio_var).pack(pady=5)

    # Spinbox
    spinbox = ttk.Spinbox(janela, from_=0, to=10, increment=1)
    spinbox.pack(pady=5)

    # Progressbar
    progress = ttk.Progressbar(janela, orient=HORIZONTAL, length=200, mode='determinate')
    progress.pack(pady=5)
    progress["value"] = 50  # Progresso inicial em 50%

    # Notebook (Abas)
    notebook = ttk.Notebook(janela)
    aba1 = Frame(notebook, bg="#f0f0f0", width=400, height=100)
    aba2 = Frame(notebook, bg="#f0f0f0", width=400, height=100)
    notebook.add(aba1, text="Aba 1")
    notebook.add(aba2, text="Aba 2")
    notebook.pack(pady=5)

    # Treeview
    tree = ttk.Treeview(janela, columns=("Coluna 1", "Coluna 2"), show="headings")
    tree.heading("Coluna 1", text="Coluna 1")
    tree.heading("Coluna 2", text="Coluna 2")
    tree.insert("", "end", values=("Dado 1", "Dado 2"))
    tree.pack(pady=5)

    janela.mainloop()

# Executar a aplicação
criar_janela_ttk()

from tkinter import *
from tkinter import ttk
from time import sleep

def criar_janela_ttk_completa():
    janela = Tk()
    janela.title("Todos os Widgets do TTK")
    janela.geometry("700x700")

    # Frame para rolagem
    container = Frame(janela)
    canvas = Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    container.pack(fill="both", expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Adiciona widgets TTK
    ttk.Label(scrollable_frame, text="Todos os Widgets Disponíveis", font=("Arial", 16)).pack(pady=10)

    # Label
    ttk.Label(scrollable_frame, text="Este é um Label").pack(pady=5)

    # Entry
    ttk.Entry(scrollable_frame).pack(pady=5)

    # Button
    ttk.Button(scrollable_frame, text="Clique Aqui").pack(pady=5)

    # Combobox
    ttk.Combobox(scrollable_frame, values=["Opção 1", "Opção 2", "Opção 3"]).pack(pady=5)

    # Checkbutton
    check_var = BooleanVar()
    ttk.Checkbutton(scrollable_frame, text="Marque-me", variable=check_var).pack(pady=5)

    # Radiobutton
    radio_var = StringVar(value="1")
    ttk.Radiobutton(scrollable_frame, text="Opção 1", value="1", variable=radio_var).pack(pady=5)
    ttk.Radiobutton(scrollable_frame, text="Opção 2", value="2", variable=radio_var).pack(pady=5)

    # Spinbox
    ttk.Spinbox(scrollable_frame, from_=0, to=10, increment=1).pack(pady=5)

    # Progressbar
    for x in range(0,101):    
        barra.config(value=x)
        sleep(delay)

    barra = ttk.Progressbar(scrollable_frame, orient=HORIZONTAL, length=200, mode='determinate', value=0)
    barra.pack(pady=5)

    # Notebook (Abas)
    notebook = ttk.Notebook(scrollable_frame)
    aba1 = Frame(notebook, bg="#f0f0f0", width=400, height=100)
    aba2 = Frame(notebook, bg="#f0f0f0", width=400, height=100)
    aba3 = Frame(notebook, bg="#f0f0f0", width=400, height=100)
    notebook.add(aba1, text="Aba 1")
    notebook.add(aba2, text="Aba 2")
    notebook.add(aba3, text="Aba 3")
    notebook.pack(pady=5)

    # Treeview
    tree = ttk.Treeview(scrollable_frame, columns=("Coluna 1", "Coluna 2"), show="headings")
    tree.heading("Coluna 1", text="Coluna 1")
    tree.heading("Coluna 2", text="Coluna 2")
    tree.insert("", "end", values=("Dado 1", "Dado 3"))
    tree.insert("", "end", values=("Dado 2", "Dado 2"))
    tree.insert("", "end", values=("Dado 3", "Dado 1"))
    tree.pack(pady=5)

    # Separator
    ttk.Separator(scrollable_frame, orient=HORIZONTAL).pack(fill="x", pady=10)

    # Panedwindow
    paned = ttk.Panedwindow(scrollable_frame, orient=HORIZONTAL)
    frame1 = ttk.Frame(paned, width=100, height=100, relief=SUNKEN)
    frame2 = ttk.Frame(paned, width=100, height=100, relief=SUNKEN)
    paned.add(frame1, weight=1)
    paned.add(frame2, weight=4)
    paned.pack(pady=10)

    # Labelframe
    labelframe = ttk.LabelFrame(scrollable_frame, text="Frame com Título")
    ttk.Label(labelframe, text="Conteúdo dentro de um LabelFrame").pack(pady=5, padx=5)
    labelframe.pack(pady=10, fill="x")

    # Scrollbar
    Label(scrollable_frame, text="Exemplo de Scrollbar").pack()
    text = Text(scrollable_frame, height=5, width=50)
    text_scrollbar = ttk.Scrollbar(scrollable_frame, orient=VERTICAL, command=text.yview)
    text.configure(yscrollcommand=text_scrollbar.set)
    text.pack(side="left", pady=10)
    text_scrollbar.pack(side="right", pady=10)

    janela.mainloop()


# Executar a aplicação
criar_janela_ttk_completa()

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def imc():
    def calcularImc():
        if peso.get() == "" or altura.get() == "":
            messagebox.showwarning("Atenção", "Dados vazios")
        else:
            peso_usu = float(peso.get())
            altura_usu = float(altura.get())
            imc = peso_usu / altura_usu ** 2
            stts = ""
            if imc < 16:
                stts = "Abaixo do peso (severo)"
            elif 16 <= imc <= 16.9:
                stts = "Abaixo do peso (moderado)"
            elif 17 <= imc <= 18.4:
                stts = "Abaixo do peso (leve)"
            elif 18.5 <= imc <= 24.9:
                stts = "Peso normal ou eutrófico"
            elif 25 <= imc <= 29.9:
                stts = "Pré-obesidade ou sobrepeso"
            elif 30 <= imc <= 34.9:
                stts = "Obesidade grau I"
            elif 35 <= imc <= 39.9:
                stts = "Obesidade grau II"
            else:
                stts = "Obesidade grau III ou mórbida"
            
            resultado.config(text=f"IMC: {imc:.2f}\n{stts}")
        
    imc = Toplevel()
    imc.title("Calcular imc")
    imc.geometry("300x350")
    imc.resizable(False, False)

    ttk.Label(imc, text="IMC", font=("EngraversGothic BT", 20)).place(x=10, y=10)
    
    Frame(imc, bg="#69a7ff").place(x=0, y=45, height=4, relwidth=.9)
    
    ttk.Label(imc, text="Informe seu peso(kg): ").place(x=10, y=60)
    peso = ttk.Entry(imc)
    peso.place(x=10, y=80, width=280, height=30)

    Label(imc, text="Informe sua altura(m): ").place(x=10, y=120)
    altura = ttk.Entry(imc)
    altura.place(x=10, y=140, width=280, height=30)
    
    ttk.Button(imc, text="Calcular IMC",command=calcularImc).place(x=10,y=200,width=135,height=40)
    ttk.Button(imc, text="Sair",command=imc.destroy).place(x=155,y=200,width=135,height=40)

    resultado = ttk.Label(imc, text="IMC",font=("EngraversGothic BT", 14,"italic"))
    resultado.place(x=10,y=260,width=280)

def regra_de_3():
    def calcular():
        try:
            # Pegando os valores inseridos
            num_A = float(num_a.get())
            num_B = float(num_b.get())
            num_C = float(num_c.get())

            # Verificando se os valores são numéricos (não é realmente necessário aqui, já que float() já valida)
            if all(isinstance(x, (int, float)) for x in (num_A, num_B, num_C)):
                # Calculando a regra de 3
                x = (num_C * num_B) / num_A

                # Atualizando o Label com o resultado
                resultado.config(text=x)

        except ValueError:
            messagebox.showerror("Atenção", "Por favor, insira valores numéricos válidos.")
        except ZeroDivisionError:
            messagebox.showerror("Erro", "O valor de A não pode ser zero.")

    # Criando a janela da regra de 3
    regra_de_3 = Toplevel()
    regra_de_3.title("Regra de três")
    regra_de_3.geometry("400x200")
    regra_de_3.resizable(False, False)

    # Labels e campos de entrada
    ttk.Label(regra_de_3, text="Num A: ").place(x=10, y=20)
    num_a = ttk.Entry(regra_de_3)
    num_a.place(x=60, y=20, height=30)

    ttk.Label(regra_de_3, text="Num B: ").place(x=200, y=20)
    num_b = ttk.Entry(regra_de_3)
    num_b.place(x=250, y=20, height=30)

    ttk.Label(regra_de_3, text="Num C: ").place(x=10, y=100)
    num_c = ttk.Entry(regra_de_3)
    num_c.place(x=60, y=100, height=30)

    # Label para o resultado
    ttk.Label(regra_de_3, text="Num X: ", font=("Arial", 12, "bold")).place(x=200, y=100)
    resultado = ttk.Label(regra_de_3, text="000")
    resultado.place(x=260, y=100)

    # Botão para calcular
    ttk.Button(regra_de_3, text="Calcular", command=calcular).place(x=10, y=150, height=40, width=380)

def calculadora():
    calculadora = Toplevel()
    calculadora.geometry("900x500")
    calculadora.resizable(False,False)
    # Função para processar os cliques nos botões
    def button_click(value):
        if value == "=":
            try:
                result = eval(entry.get())
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
            except Exception:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Erro")
        elif value == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, value)

    # Configuração da janela principal

    # Entrada para mostrar os números e o resultado
    entry = ttk.Entry(calculadora, font=("Arial", 16), justify="right")
    entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")

    # Botões da calculadora
    buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "C", "0", "=", "+"
    ]

    # Configuração dos botões na grade
    for i, btn in enumerate(buttons):
        ttk.Button(calculadora, text=btn, command=lambda b=btn: button_click(b)).grid(
            row=(i // 4) + 1, column=i % 4, padx=2, pady=2, sticky="nsew"
        )

    # Configuração das proporções das colunas e linhas
    for i in range(4):
        calculadora.grid_columnconfigure(i, weight=1)
    for i in range(5):
        calculadora.grid_rowconfigure(i, weight=1)


# Janela principal
janela = Tk()

janela.title("Minha primeira janela no Tkinter")
janela.geometry("800x500")
janela.resizable(False, False)
janela.configure()

Frame(janela, bg="#69a7ff").place(x=0, y=45, height=4, relwidth=.9)

ttk.Label(janela, text="Calculadora", font=("EngraversGothic BT", 18)).place(x=10, y=10)

ttk.Button(janela, text="IMC", command=imc).place(x=10, y=55, width=150, height=40)
ttk.Button(janela, text="Regra de 3", command=regra_de_3).place(x=160, y=55, width=150, height=40)
ttk.Button(janela, text="Calculadora", command=calculadora).place(x=310, y=55, width=150, height=40)

ttk.Label(janela, text="Autor: Ivande", font=("EngraversGothic BT", 12)).place(x=690, y=475)

janela.mainloop()

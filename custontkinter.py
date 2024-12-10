import customtkinter as ctk

# pip install customtkinter
# pip install customtkinter --upgrade

def button_callback():
    print("button pressed")

app = ctk.CTk()
app.title("my app")
app.geometry("400x150")

lbl_nome = ctk.CTkLabel(app, text="Nome")
lbl_nome.grid(row=0, column=0, padx=20, pady=20)

input_nome = ctk.CTkEntry(app)
input_nome.grid(row=0, column=1, padx=20, pady=20)

button = ctk.CTkButton(app, text="my button", command=button_callback)
button.grid(row=1, column=0, padx=20, pady=20)

app.mainloop()
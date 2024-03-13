import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print("Fazer Login")


texto = customtkinter.CTkLabel(janela, text="Bem Vindo(a) ao Liriobranco Atelier")
texto.pack(padx=10, pady=10)

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)
cpf = customtkinter.CTkEntry(janela, placeholder_text="Insira seu CPF")
cpf.pack(padx=10, pady=10)


senha = customtkinter.CTkEntry(janela, placeholder_text="Insira sua senha", show="*")
senha.pack(padx=10, pady=10)


checkBox = customtkinter.CTkCheckBox(janela, text="Lembrar login")
checkBox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)


janela.mainloop()
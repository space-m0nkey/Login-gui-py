import customtkinter
import tkinter.messagebox
from keyauth import api
import hashlib
import sys

def calcular_checksum():
    md5_hash = hashlib.md5()
    arquivo = open(''.join(sys.argv), "rb")
    md5_hash.update(arquivo.read())
    digest = md5_hash.hexdigest()
    return digest
keyauthapp = api(
    name="reverse",
    ownerid="h4GlGtPhNA",
    secret="fa3158db3ec9df08dbe8ad4dc4d2f68b93b654a55e2013236cbdd455dc05799f",
    version="1.0",
    hash_to_check=calcular_checksum()
)
def login():
        keyauthapp.login(usuario.get(), senha.get())
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
janela= customtkinter.CTk()
janela.geometry("500x300")
txt= customtkinter.CTkLabel(janela,text="Fazer login")
txt.pack(padx=10,pady=10)
usuario= customtkinter.CTkEntry(janela,placeholder_text="Seu usuario")
usuario.pack(padx=10,pady=10)
senha= customtkinter.CTkEntry(janela,placeholder_text="sua senha",show="*")
senha.pack(padx=10,pady=10)
blos= customtkinter.CTkButton(janela,text="login",command=login)
blos.pack(padx=10,pady=10)

janela.mainloop()
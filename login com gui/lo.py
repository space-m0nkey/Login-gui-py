import customtkinter
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
    name="",
    ownerid="",
    secret="",
    version="1.0",
    hash_to_check=calcular_checksum()
)
def login():
        keyauthapp.login(usuario.get(), senha.get())
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
janela= customtkinter.CTk()
janela.geometry("500x300")
janela.resizable(width=False, height=False)
janela.iconbitmap("key.ico")
janela.title("Login")
txt= customtkinter.CTkLabel(janela,text="Fazer login")
txt.pack(padx=10,pady=10)
usuario= customtkinter.CTkEntry(janela,placeholder_text="Seu usuario")
usuario.pack(padx=10,pady=10)
senha= customtkinter.CTkEntry(janela,placeholder_text="sua senha",show="*")
senha.pack(padx=10,pady=10)
blos= customtkinter.CTkButton(janela,text="login",command=login)
blos.pack(padx=10,pady=10)

janela.mainloop()

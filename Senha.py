from tkinter import *
import datetime
import os

def Atualizar():
    global dataAtual, dia, mes, ano, hora, anoF, senhaUnico, senhaSaurus, senhaChef
    dataAtual = datetime.datetime.now()
    dia = dataAtual.day
    mes = dataAtual.month
    ano = dataAtual.year
    hora = dataAtual.hour
    anoF = (dataAtual.year - 2000)

    senhaUnico = (dia * mes * anoF * 3)
    senhaSaurus = str(dia + mes) + str(hora + 10)
    digitoChef = (dia + ano + mes) * 7
    senhaChef = str(digitoChef)[-2:] + str(ano)[-2:] + f"{mes:02d}" + f"{dia:02d}"
    texto2.config(text=f"{senhaUnico}")
    texto4.config(text=f"@{senhaSaurus}")
    texto6.config(text=f"{senhaChef}")

dataAtual = datetime.datetime.now()
dia = dataAtual.day
mes = dataAtual.month
ano = dataAtual.year
hora = dataAtual.hour
anoF = (dataAtual.year - 2000)

dataF = dataAtual.strftime("%d/%m/%y")
senhaUnico = (dia * mes * anoF * 3)
senhaSaurus = str(dia + mes) + str(hora + 10)
digitoChef = (dia + ano + mes) * 7
senhaChef = str(digitoChef)[-2:] + str(ano)[-2:] + f"{mes:02d}" + f"{dia:02d}"

window = Tk()
icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
window.iconbitmap(icon_path)
window.title('Password')
window.geometry("240x360+1+1")
window.wm_maxsize(width=240, height=360)
window.wm_minsize(width=240, height=360)
window.resizable(width=False, height=False)
window.config(background="#e84343")


texto1 = Label(text='Unico', font=("Verdana", 13), bg='#e84343', fg='#ffffff')
texto2 = Label(text=f"{senhaUnico}", font=("Arial Black", 30), bg='#e84343', fg='#ffffff')
texto3 = Label(text='Saurus', font=("Verdana", 13), bg='#e84343', fg='#ffffff')
texto4 = Label(text=f"@{senhaSaurus}", font=("Arial Black", 30), bg='#e84343', fg='#ffffff')
texto5 = Label(text='Totvs Chef', font=("Verdana", 13), bg='#e84343', fg='#ffffff')
texto6 = Label(text=f"{senhaChef}", font=("Arial Black", 30), bg='#e84343', fg='#ffffff')
botao1 = Button(text='Atualizar', font=("Arial", 15), bg='white', command=Atualizar)
creditos = Label(text='by Pedro Alexandre', font=("Arial", 10), bg='#e84343', fg='#ffffff')

texto1.pack(pady=(7,0))
texto2.pack()
texto3.pack(pady=(0,0))
texto4.pack()
texto5.pack(pady=(0,0))
texto6.pack()
botao1.pack(pady=(7,0))
creditos.pack(pady=(4,0))

window.mainloop()

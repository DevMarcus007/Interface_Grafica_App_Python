# Aplicativo de apoio ao monitoramento de SEDEX 

# Importações------------------------------------------

from tkinter import *
from tkinter import filedialog as dlg
from time import sleep
import pandas as pd

# Funções ---------------------------------------------

def carregarArquivo ():
    global objetos 
    objetos = pd.read_excel (dlg.askopenfilename(), sheet_name = 2)
    return objetos

def rodarPlanilha():
    matriz = objetos[["Objeto", "Situação"]]
    print(matriz)

def enviarEmail():
    print()

def escreverEmail():
    print()

# Interface Gráfica -----------------------------------

root = Tk()

#Janela principal
root.title = "Monitoramento SEDEX"
root.geometry("480x360+300+300")
root["bg"] = "grey"

#Botões
carregar_arquivo = Button(root,
             text="Carregar Arquivo Macro",
             command = carregarArquivo)

rodar_planilha = Button(root,
             text="Rodar Planilha",
             command = rodarPlanilha)

enviar_email = Button(root,
             text="Enviar E-mail",
             command = enviarEmail)

#Labels

top = Label(root,
            text = "-----MONITORAMENTO SEDEX - GERAE 05-----",
            bg = "grey",
            bd = 2,
            font = 65,
            relief = SOLID) 

# Frame das unidades

##Verificar video 30 João Ribeiro

#Instanciar widgets

top.grid(row=0, columnspan=4)

carregar_arquivo.grid(row=1,columnspan=2)
rodar_planilha.grid(row=2,column=0)
enviar_email.grid(row=2,column=1)





root.mainloop()
## OK da planilha e do email enviado, criar função com If Else
# Aplicativo de apoio ao monitoramento de SEDEX 

# Importações------------------------------------------

from tkinter import *
from tkinter import filedialog as dlg
import pandas as pd


# Variáveis -------------------------------------------

objetos = 0


# Funções ---------------------------------------------

def carregarArquivo ():
    objetos = pd.read_excel (dlg.askopenfilename(), sheet_name = "Dados Benfica")
    #arquivo = pd.read_excel(objetos, sheet_name = "Dados Benfica")
    print(objetos)

def rodarPlanilha():
    print()

def enviarEmail():
    print()

def escreverEmail():
    print()

# Interface Gráfica -----------------------------------

root = Tk()

#Janela principal
root.title = "Monitoramento SEDEX"
root.geometry("640x480+300+300")
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
            text = "MONITORAMENTO SEDEX - GERAE 05",
            bg = "grey",
            bd = 1,
            relief = SOLID) 

# Frame das unidades

##Verificar video 30 João Ribeiro
frame_unidades = Frame(root,
                       bg="grey")

pcb = Label(frame_unidades, text = "AC Paracambi", bg="grey").grid(row=0,column=0,sticky=W)
pcb_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=0,column=1,sticky=E)
aps = Label(frame_unidades, text = "CDD Alto da Posse", bg="grey").grid(row=1,column=0,sticky=W)
aps_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=1,column=1,sticky=E)
brx = Label(frame_unidades, text = "CDD Belford Roxo", bg="grey").grid(row=2,column=0,sticky=W)
brx_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=2,column=1,sticky=E)
cbu = Label(frame_unidades, text = "CDD Cabuçu", bg="grey").grid(row=3,column=0,sticky=W)
cbu_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=3,column=1,sticky=E)
cps = Label(frame_unidades, text = "CDD Campos Eliseos", bg="grey").grid(row=4,column=0,sticky=W)
cps_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=4,column=1,sticky=E)
ctn = Label(frame_unidades, text = "CDD Centenário", bg="grey").grid(row=5,column=0,sticky=W)
ctn_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=5,column=1,sticky=E)
cos = Label(frame_unidades, text = "CDD Comendador Soares", bg="grey").grid(row=6,column=0,sticky=W)
cos_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=6,column=1,sticky=E)
ddx = Label(frame_unidades, text = "CDD Duque de Caxias", bg="grey").grid(row=7,column=0,sticky=W)
ddx_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=7,column=1,sticky=E)
mge = Label(frame_unidades, text = "CDD Magé", bg="grey").grid(row=8,column=0,sticky=W)
mge_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=8,column=1,sticky=E)
msq = Label(frame_unidades, text = "CDD Mesquita", bg="grey").grid(row=9,column=0,sticky=W)
msq_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=9,column=1,sticky=E)
nlp = Label(frame_unidades, text = "CDD Nilópolis", bg="grey").grid(row=10,column=0,sticky=W)
nlp_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=10,column=1,sticky=E)
nig = Label(frame_unidades, text = "CDD Nova Iguaçu", bg="grey").grid(row=11,column=0,sticky=W)
nig_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=11,column=1,sticky=E)
psv = Label(frame_unidades, text = "CDD Parque São Vicente", bg="grey").grid(row=12,column=0,sticky=W)
psv_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=12,column=1,sticky=E)
qmd = Label(frame_unidades, text = "CDD Queimados", bg="grey").grid(row=13,column=0,sticky=W)
qmd_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=13,column=1,sticky=E)
scs = Label(frame_unidades, text = "CDD Santa Cruz da Serra", bg="grey").grid(row=14,column=0,sticky=W)
scs_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=14,column=1,sticky=E)
sjm = Label(frame_unidades, text = "CDD São João de Meriti", bg="grey").grid(row=15,column=0,sticky=W)
sjm_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=15,column=1,sticky=E)
vcv = Label(frame_unidades, text = "CDD Vila de Cava", bg="grey").grid(row=16,column=0,sticky=W)
vcv_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=16,column=1,sticky=E)
vtl = Label(frame_unidades, text = "CDD Vilar dos Teles", bg="grey").grid(row=17,column=0,sticky=W)
vtl_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=17,column=1,sticky=E)
cee = Label(frame_unidades, text = "CEE Nova Iguaçu", bg="grey").grid(row=18,column=0,sticky=W)
cee_ok = Label(frame_unidades, text = "   ", bg="grey", bd=1, relief=GROOVE).grid(row=18,column=1,sticky=E)


#Instanciar widgets

top.grid(columnspan=3)

carregar_arquivo.grid(row=1,columnspan=2)
rodar_planilha.grid(row=2,column=0)
enviar_email.grid(row=2,column=1)

frame_unidades.grid(row=4,column=0)




root.mainloop()
## OK da planilha e do email enviado, criar função com If Else
from tkinter import *
from tkinter import filedialog as dlg
import pandas as pd
from pandas.io.stata import StataWriterUTF8

tela_inicio = Tk()

tela_inicio.title ("Monitoramento SEDEX") #Definir o título da janela
tela_inicio.geometry("500x300+300+300") #Definir o tamanho e a posição da janela 
tela_inicio['bg'] = "gray" #definir o background color

#criar o label, mas não instanciar. A ordem dos instanciamentos importa se utilizar o pack()
objetos = 0
label_1 = Label(tela_inicio, 
                text = "",
                bg = "grey",#backgroud color
                fg = "blue",#cor da fonte
                font = "Comics 15 bold",#definição da fonte, tamanho e negrito
                width = 20,#largura
                height = 1,#altura
                borderwidth = 1, #pode ser representado como bd = 1
                relief="flat",#obrigatório para colocar a borda
                )

label_2 = Label(tela_inicio, 
                text = "",
                bg = "grey",#backgroud color
                fg = "blue",#cor da fonte
                font = "Comics 15 bold",#definição da fonte, tamanho e negrito
                width = 20,#largura
                height = 1,#altura
                borderwidth = 1, #pode ser representado como bd = 1
                relief="flat",#obrigatório para colocar a borda
                )


#criar a função do click no botão
def cmd_Click():
    label_1 ['text'] = "Ola Mundo!" 
    label_1 ['relief'] = "solid"
    label_2 ['text'] = textbox1.get()


def abrirPasta():
    objetos = pd.read_excel(dlg.askopenfile())

#lista os atributos e respectivos valores do widget (no console)
for item in label_1.keys():
    print(f'{item} : {label_1[item]}')
    
#criar o botão
cmd = Button(tela_inicio, text = "Executar", command = cmd_Click)
cmd2 = Button(tela_inicio, text = "Informar Arquivo", command = abrirPasta)

#instanciar o botão. poderia utilizar o cmd.pack() sem parametros
cmd.grid(row=0, column=1)
cmd2.grid(row=0, column=2)

#instanciar o label utilizando o grid, para configurar o posicionamento. columnspan junta mais de uma linha.
label_1.grid(columnspan=2)
label_2.grid(row=2, column=0)

#criar e instanciar a textbox direto
textbox1 = Entry(tela_inicio)
textbox1.grid(row=0, column=0, sticky=W)

print(objetos)

#comando obrigatório para não fechar a janela imediatamente   
tela_inicio.mainloop()

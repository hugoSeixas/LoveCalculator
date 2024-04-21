# importando a janela

from tkinter import *
from tkinter import Tk, ttk

# importando as configurações da janela

from PIL import Image, ImageTk

import random

#cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#93A3B1"   # verde


# criando janela ----------------------
janela = Tk()
janela.title("")
janela.geometry('410x400')
janela.configure(background=co1)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use('clam')


# frames -----------------------------
frameCima = Frame(janela, width=418, height=200, bg=co1)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=418, height=200, bg=co1, relief='solid')
frameMeio.grid(row=1, column=0)


# logo ---------------------------------
app_ = Label(frameCima, text='Love Calculator', width=400, padx=5, anchor=NW, font=('Fixedsys 20'), bg=co7, fg=co1)
app_.place(x=0, y=0)


# funcao calcular amor
def calcular_amor():
    # pegando nomes
    nome_1 = seu_nome.get()
    nome_2 = parceiro_nome.get()

    # valor conterá digitos de 0 até 9
    st = '0123456789'

    # resultado sera em dois digitos
    digitos = 2

    # variavel que contem o resultado
    resultado = "".join(random.sample(st, digitos))

    l_result['text'] = 'Porcentagem de amor entre'
    l_result1['text'] = nome_1 + " & " + nome_2
    l_result2['text'] = resultado + "%"


# Funcao para escolher opçoes -----------------
def escolher():
    # variaveis globais
    global app_img, app_love

    escolha_1 = selecionado_1.get()
    escolha_2 = selecionado_2.get()

    if escolha_1 == 'Homem' and escolha_2 == 'Mulher':
        imagem = './img/casal1.png'
        imagem_2 = './img/heart2.png'
    elif escolha_1 == 'Homem' and escolha_2 == 'Homem':
        imagem = './img/gay.png'
        imagem_2 = './img/heart3.png'
    elif escolha_1 == 'Mulher' and escolha_2 == 'Homem':
        imagem = './img/casal.png'
        imagem_2 = './img/heart2.png'
    elif escolha_1 == 'Mulher' and escolha_2 == 'Mulher':
        imagem = './img/lesb.png'
        imagem_2 = './img/heart3.png'
    else:
        print('Selecione os generos')
        return


    # abrindo imagem casal-------------------------
    app_img = Image.open(imagem)
    app_img = app_img.resize((140, 140))
    app_img = ImageTk.PhotoImage(app_img)
    app_logo['image'] = app_img

    # abrindo imagem botao-------------------------
    app_love = Image.open(imagem_2)
    app_love = app_love.resize((30, 30))
    app_love = ImageTk.PhotoImage(app_love)
    button['image'] = app_love

# abrindo imagem -------------------------
app_img = Image.open('./img/heart.png')
app_img = app_img.resize((140, 140))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT,  padx=5, anchor=NW, bg=co1, fg=co4)
app_logo.place(x=10, y=50)


# Resultados ---------------------------------
l_result = Label(frameCima, text='', width=35, padx=10, anchor=NW, font=('Verdana 10'), bg=co1, fg=co0)
l_result.place(x=170, y=70)

l_result1 = Label(frameCima, text='', width=17, padx=10, anchor=CENTER, font=('Verdana 12 bold'), bg=co1, fg=co5)
l_result1.place(x=170, y=100)

l_result2 = Label(frameCima, text='', width=5, padx=10, anchor=CENTER, font=('Verdana 25 bold'), bg=co1, fg=co0)
l_result2.place(x=210, y=140)

# frame meio ----------------------------
l_nome = Label(frameMeio, text='Seu nome', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=6, y=15)

seu_nome = Entry(frameMeio, width=15, font=('Ivy 14'), justify='center', relief='solid')
seu_nome.place(x=10, y=40)

selecionado_1 = StringVar()

rad_1 = Radiobutton(frameMeio, command=escolher, text='Homem', bg=co1, font=('Ivy 10'), value='Homem', variable=selecionado_1).place(x=10, y=80)
rad_2 = Radiobutton(frameMeio,command=escolher, text='Mulher', bg=co1, font=('Ivy 10'), value='Mulher', variable=selecionado_1).place(x=10, y=105)

l_linha = Label(frameMeio, width=1, height=10, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
l_linha.place(x=190, y=40)
l_linha = Label(frameMeio, width=1, height=10, anchor=NW, font=('Verdana 1'), bg=co5, fg=co1)
l_linha.place(x=200, y=40)

l_nome = Label(frameMeio, text='Nome do/a parceiro/a', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=217, y=15)

parceiro_nome = Entry(frameMeio, width=15, font=('Ivy 14'), justify='center', relief='solid')
parceiro_nome.place(x=220, y=40)

selecionado_2 = StringVar()

rad_3 = Radiobutton(frameMeio,command=escolher, text='Homem', bg=co1, font=('Ivy 10'), value='Homem', variable=selecionado_2).place(x=220, y=80)
rad_4 = Radiobutton(frameMeio,command=escolher, text='Mulher', bg=co1, font=('Ivy 10'), value='Mulher', variable=selecionado_2).place(x=220, y=105)


# botao calcular ---------------------------
app_love = Image.open('img/cupid.png')
app_love = app_love.resize((30, 30))
app_love = ImageTk.PhotoImage(app_love)

button = Button(frameMeio,command=calcular_amor, image=app_love, width=200, compound=LEFT, text='Calcular Amor'.upper(), anchor=CENTER, font=('Ivy 9'), bg=co2, fg=co1)
button.place(x=110, y=140)

janela.mainloop()

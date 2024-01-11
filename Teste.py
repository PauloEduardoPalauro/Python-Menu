import tkinter as tk
from tkinter import *
from tkinter import messagebox
from customtkinter import *
from pytube import YouTube
from PIL import Image, ImageTk
from PyDictionary import PyDictionary 
import pyttsx3




# Sobre a Janela
janela = CTk()
janela.title('Python Menu')
janela.geometry('500x250')

set_appearance_mode("dark")
set_default_color_theme("blue")


def abrirProg():
    nome = entry.get()
    if not nome:
        messagebox.showwarning("Aviso", "Por favor, digite seu nome.")
    else:
        # Criar a nova janela
        prog = CTk()    
        prog.title("Nova Janela")
        prog.geometry("800x500")

        # Exibir a mensagem de boas-vindas com o nome digitado
        label_menu = CTkLabel(prog, text="Python Menu", font=('Helvetica', 20))
        label_menu.pack(side=tk.LEFT, anchor='nw', padx=10, pady=10)

        label_nome = CTkLabel(prog, text="Seja Bem-vindo: " + nome, font=('Helvetica', 15))
        label_nome.pack(side=tk.RIGHT, anchor='ne', padx=10, pady=10)
        CTkButton(prog, text="Paint", font=('Helvetica', 20), command=paint, height=40, width=400, corner_radius=32, fg_color="#4158D0").pack(pady=10)
        CTkButton(prog, text="Download Youtube video", font=('Helvetica', 20), command=yt_Video, height=40, width=400, corner_radius=32, fg_color="#4158D0").pack(pady=10)
        CTkButton(prog, text="Audio Dicionario", font=('Helvetica', 20), command=dicionario, height=40, width=400, corner_radius=32, fg_color="#4158D0").pack(pady=10)
        CTkButton(prog, text="Paint", font=('Helvetica', 20), command=paint, height=40, width=400, corner_radius=32, fg_color="#4158D0").pack(pady=10)



def fecharJanela():
    if messagebox.askokcancel("Fechar", "Tem certeza que quer sair?"):
        janela.destroy()


def paint():
    # setup
    janela_paint = CTkToplevel()
    janela_paint.geometry('600x400')
    janela_paint.title('Canvas')

    # canvas 
    canvas = CTkCanvas(janela_paint, bg='white', width=500, height=300)
    canvas.pack(anchor="center", pady=50)

    def draw_on_canvas(event):
        x = event.x
        y = event.y
        canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill='black')

    def brush_size_adjust(event):
        global brush_size
        if event.delta > 0:
            brush_size += 4
        else:
            brush_size -= 4 

        brush_size = max(0, min(brush_size, 50))

    brush_size = 2
    canvas.bind('<Motion>', draw_on_canvas)
    canvas.bind('<MouseWheel>', brush_size_adjust)

    


def yt_Video():
    yt = CTkToplevel()    
    yt.title("Nova Janela")
    yt.geometry("900x600")

    def startDownload():
        try:
            yt_link = link.get()
            yt_object = YouTube(yt_link)
            video = yt_object.streams.get_highest_resolution()
            video.download()
        except:
            pronto.configure(text="Error no Download!")
        pronto.configure(text="Baixado!")
        

    def startMP3():
        try:
            yt_link = link.get()
            yt_object = YouTube(yt_link)
            mp3 = yt_object.streams.filter(only_audio=True).first()
            mp3.download()
            pronto.configure(text="MP3 Baixado!")
        except Exception as e:
            pronto.configure(text=f"Error ao converter para MP3: {e}")


    my_image = CTkImage(light_image=Image.open('images/yt.png'),
    dark_image=Image.open('images/yt.png'),
	size=(400,200)) # WidthxHeight

    my_label = CTkLabel(yt, text="", image=my_image)
    my_label.pack(pady=10)

    CTkLabel(yt, text="Insira um link do Youtube abaixo", font=('Helvetica', 20)).pack(pady=20)

    link = CTkEntry(master = yt, width=500, placeholder_text="Insira URL")
    link.pack()

    pronto = CTkLabel(yt, text="", font=('Helvetica' , 12))
    pronto.pack(pady=5)

    download = CTkButton(yt, text="Download", command=startDownload,  fg_color="#4158D0", width=250, height=40, font=('Helvetica', 20, "bold") ).pack(pady=30)
    audio = CTkButton(yt, text="Download audio", command=startMP3,  fg_color="#4158D0" , width=250, height=40, font=('Helvetica', 20, "bold")).pack(pady=20)


def dicionario():
    dici = CTkToplevel()
    dici.title("Nova Janela")
    dici.geometry("900x600")

    def signi():
        try:
            palavra = pala.get()
            meaning = dict.meaning(palavra)
            result_text.delete(1.0, "end")
            result_text.insert("end", str(meaning))
        except Exception as e:
            print("Erro:", e)


    def ouvir():
        try:
            ler = result_text.get(1.0, "end-1c")
            engine.say(ler)
            engine.runAndWait()

        except:
            print("cu")
   
    dict = PyDictionary()
    engine = pyttsx3.init()

    CTkLabel(dici, text="Audio Dicionario", font=('Helvetica', 80, 'bold')).pack(pady=20)

    pala = CTkEntry(dici, width=500, placeholder_text="DIGITE A PALAVRA EM INGLÊS!")
    pala.pack(pady=20, padx=10)

    CTkButton(dici, text="Traduzir", command=signi, corner_radius=32, fg_color="#4158D0").pack(pady=10)

    result_text = CTkTextbox(dici, width=600, height=300)
    result_text.pack()

    CTkButton(dici, text="Ler", command=ouvir, corner_radius=32, fg_color="#4158D0").pack(pady=10)
    

#janela.protocol("WM_DELETE_WINDOW", fecharJanela)

CTkLabel(janela, text= "Digite seu nome e clique no Botão para prosseguir", font= ('Helvetica', 20)).pack(pady=40)

entry = CTkEntry(master = janela)
entry.pack()
 
CTkButton(janela, text="Abrir", command=abrirProg, corner_radius=32, fg_color="#4158D0", font= ('Helvetica', 20,'bold') ).pack(pady=10)


janela.mainloop()
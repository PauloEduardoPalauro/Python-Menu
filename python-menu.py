import tkinter as tk
from tkinter import *
from tkinter import messagebox
from customtkinter import *
from pytube import YouTube
from PIL import Image, ImageTk
from PyDictionary import PyDictionary 
import pyttsx3
import os
import requests
from io import BytesIO
import pyautogui

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
        label_menu = CTkLabel(prog, text="Python Menu", font=('Helvetica', 20, 'bold'))
        label_menu.pack(side=tk.LEFT, anchor='nw', padx=10, pady=10)

        label_nome = CTkLabel(prog, text="Seja Bem-vindo: " + nome, font=('Helvetica', 15))
        label_nome.pack(side=tk.RIGHT, anchor='ne', padx=10, pady=10)
        CTkButton(prog, text="Paint", font=('Helvetica', 20, 'bold'), command=paint, height=40, width=400, corner_radius=32, fg_color="#4158D0").pack(pady=30)
        CTkButton(prog, text="Download Youtube video", font=('Helvetica', 20, 'bold' ), command=yt_Video, height=40, width=400, corner_radius=32, fg_color="#4158D0").pack(pady=30)
        CTkButton(prog, text="Audio Dicionario", font=('Helvetica', 20, 'bold'), command=dicionario, height=40, width=400, corner_radius=32, fg_color="#4158D0").pack(pady=30)
        CTkButton(prog, text="Clima", font=('Helvetica', 20, 'bold'), command=clima, height=40, width=400, corner_radius=32, fg_color="#4158D0").pack(pady=30)
        CTkButton(prog, text="Captura de Tela", font=('Helvetica', 20, 'bold'), command=screen, height=40, width=400, corner_radius=32, fg_color="#4158D0").pack(pady=30)



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
    yt.geometry("900x650")

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


    my_image = CTkImage(light_image=Image.open('images/yt2.png'),
    dark_image=Image.open('images/yt2.png'),
	size=(400,300)) # WidthxHeight

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
            print("Não foi possivel ler!")
   
    dict = PyDictionary()
    engine = pyttsx3.init()

    CTkLabel(dici, text="Audio Dicionario", font=('Helvetica', 80, 'bold')).pack(pady=20)

    pala = CTkEntry(dici, width=500, placeholder_text="DIGITE A PALAVRA EM INGLÊS!")
    pala.pack(pady=20, padx=10)

    CTkButton(dici, text="Traduzir", command=signi, corner_radius=32, fg_color="#4158D0").pack(pady=10)

    result_text = CTkTextbox(dici, width=600, height=300)
    result_text.pack()

    CTkButton(dici, text="Ler", command=ouvir, corner_radius=32, fg_color="#4158D0").pack(pady=10)
    


def clima():
    climaW= CTkToplevel()
    climaW.title("GPT")
    climaW.geometry("560x360")

    def pegar_clima(cidade):
            api_key = '0634ea20b51063b31966eb3facbd8e50'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}'
            res = requests.get(url)

            if res.status_code == 404:
                messagebox.showerror("Erro", "Cidade não encontrada")
                return None
            
            climaR = res.json()
            icon_id = climaR['weather'][0]['icon']
            temperatura = climaR['main']['temp'] - 273.15
            descrição = climaR['weather'][0]['description']
            city = climaR['name']
            pais = climaR['sys']['country']

            icon_url = f'https://openweathermap.org/img/wn/{icon_id}@2x.png'
            return (icon_url, temperatura, descrição, city, pais)


    def pesquisa():
            cidade = cidade_entry.get()
            resultado = pegar_clima(cidade)
            if resultado is None:
                return

            icon_url, temperatura, descrição, city, pais = resultado
            local_label.configure(text=f"{city}, {pais}")

            response = requests.get(icon_url, stream=True)
    
            if response.status_code == 200:
                # Use BytesIO to create a stream of image data
                image_data = BytesIO(response.content)
                
                try:
                    # Open the image using Pillow
                    image = Image.open(image_data)

                    # Create an ImageTk object to display in the Tkinter window
                    icon = ImageTk.PhotoImage(image)
                    icon_label.configure(image=icon)
                    icon_label.image = icon
                except Exception as e:
                    print(f"Error opening image: {e}")
            else:
                print(f"Failed to fetch image. Status code: {response.status_code}")

            temperatura_label.configure(text=f"Temperatura: {temperatura:.2f} C")

            descrição_label.configure(text=f"Descrição: {descrição}")


    CTkLabel(climaW, text= "Digite o nome da cidade", font= ('Helvetica', 20)).pack(pady=10)
    cidade_entry = CTkEntry(master= climaW)
    cidade_entry.pack()

    CTkButton(climaW, text="Procurar", command=pesquisa, corner_radius=32, fg_color="#4158D0", font= ('Helvetica', 20,'bold') ).pack(pady=20)

    local_label = CTkLabel(climaW, font= ('Helvetica', 20), text="")
    local_label.pack(pady=10)

    icon_label = CTkLabel(climaW, text="")
    icon_label.pack()

    temperatura_label = CTkLabel(climaW, font= ('Helvetica', 20), text="")
    temperatura_label.pack()

    descrição_label = CTkLabel(climaW, font= ('Helvetica', 20), text="") 
    descrição_label.pack()


def screen():
    screenW= CTkToplevel()
    screenW.title("Captura de Tela")
    screenW.geometry("600x400")


    def printscreen():
        captura = pyautogui.screenshot()
        diretorio = filedialog.asksaveasfilename(defaultextension='.png')
        captura.save(diretorio)


    my_image = CTkImage(light_image=Image.open('images/camera.png'),
    dark_image=Image.open('images/camera.png'),
	size=(400,300)) # WidthxHeight

    my_label = CTkLabel(screenW, text="", image=my_image)
    my_label.pack(pady=10)


    CTkButton(screenW, text="Capturar Tela", command=printscreen, corner_radius=32, fg_color="#4158D0", font= ('Helvetica', 20,'bold'), anchor=CENTER ).pack(pady=25)

    



#janela.protocol("WM_DELETE_WINDOW", fecharJanela)

CTkLabel(janela, text= "Digite seu nome e clique no Botão para prosseguir!", font= ('Helvetica', 19, 'bold')).pack(pady=40)

entry = CTkEntry(master = janela, width=300)
entry.pack()
 
CTkButton(janela, text="Abrir", command=abrirProg, corner_radius=32, fg_color="#4158D0", font= ('Helvetica', 15,'bold') ).pack(pady=30)


janela.mainloop()
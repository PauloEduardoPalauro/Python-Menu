import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Sobre a Janela
janela = Tk()
janela.title('Python Menu')
janela.geometry('500x250')


def abrirProg():
    nome = entry.get()
    if not nome:
        messagebox.showwarning("Aviso", "Por favor, digite seu nome.")
    else:
        # Criar a nova janela
        prog = tk.Toplevel(janela)    
        prog.title("Nova Janela")
        prog.geometry("800x500")

        # Exibir a mensagem de boas-vindas com o nome digitado
        label_menu = Label(prog, text="Python Menu", font=('Helvetica 20 bold'))
        label_menu.pack(side=tk.LEFT, anchor='nw', padx=10, pady=10)

        label_nome = Label(prog, text="Seja Bem-vindo " + nome, font=('Helvetica 15 bold'))
        label_nome.pack(side=tk.RIGHT, anchor='ne', padx=10, pady=10)
        Button(prog, text="Paint", font=('Helvetica 20'), command=paint, height=1, width=20).pack(pady=10)
        Button(prog, text="Open", command=abrirProg, ).pack(pady=10)
        Button(prog, text="Open", command=abrirProg, ).pack(pady=10)
        Button(prog, text="Open", command=abrirProg, ).pack(pady=10)



def fecharJanela():
    if messagebox.askokcancel("Fechar", "Tem certeza que quer sair?"):
        janela.destroy()


def paint():
    # setup
    janela_paint = tk.Tk()
    janela_paint.geometry('600x400')
    janela_paint.title('Canvas')

    # canvas 
    canvas = tk.Canvas(janela_paint, bg='white', width=500, height=300)
    canvas.pack()

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

    

   



janela.protocol("WM_DELETE_WINDOW", fecharJanela)

Label(janela, text= "Digite seu nome e clique no Botão para prosseguir", font= ('Helvetica 10 bold')).pack(pady=40)

entry = tk.Entry(master = janela)
entry.pack()
 
tk.Button(janela, text="Open", command=abrirProg, ).pack(pady=10)


janela.mainloop()
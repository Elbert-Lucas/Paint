from tkinter import *
import asyncio

brush_size = 20

async def new_draw(*locations):
    #UNE OS PONTOS POR UMA LINHA PARA MELHORAR O TRAÇO, E RESETA PARA UM NOVO TRAÇO
        #PRIMEIRO INDEX DA MATRIZ GUARDA OS PONTOS, O SEGUNDO GUARDA O X E Y DE CADA PONTO
    if not circle[0]:
        pass
    else:
        canvas.create_line(circle[0][0], circle[0][1],
                          locations[0], locations[1], width=brush_size, fill="black")

    circle[0] = list(locations)

def draw(event):
    #DESENHA OS PONTOS E GUARDA SUAS POSIÇOES
    x, y = event.x, event.y

    #FUNÇÃO PARA DEIXAR A LINHA NO MEIO DO PONTO

    canvas.create_oval(x,y, x+brush_size, y+brush_size, fill="black", outline="")
    asyncio.run(new_draw(x+brush_size/2,y+brush_size/2))

def end(event):
    circle[0].clear()

window = Tk()
window.geometry("1200x800")
canvas = Canvas(window, width=1200, height=800, bg="white")
canvas.pack(pady=0)

circle = [[]]

window.bind("<B1-Motion>", draw)
window.bind("<ButtonRelease-1>", end)
window.mainloop()

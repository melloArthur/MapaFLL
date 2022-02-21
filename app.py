from tkinter import *
from math import sqrt, acos, degrees
from PIL import Image
from PIL import ImageTk
from random import randint

dados_reta = []

comp_real = 200 #Comprimento real da mesa (cm)
tam_robo = 20 #Tamanho do robô (cm)

tex = open(f'{randint(1,10000000)}.txt','w+')
print(f'Arquivo gerado: {tex.name}')


def CalcDist(xi, yi, xf, yf): #Função para o cálculo das distâncias
    return sqrt((xf-xi) ** 2 + (yf-yi) ** 2)


def CalcAngulo(c1, c2, v1, v2, d1, d2): #Função para o cálculo do ângulo
    cosAngulo = (c1 * c2 + v1 * v2) / (d1 * d2)
    return round(degrees(acos(cosAngulo)), 2)


def draw_line(event): #Função para o desenho da linha
    global click_number
    global x1, y1 #Pega as coordenadas do primeiro ponto
    if click_number == 0:
        x1 = event.x
        y1 = event.y
        click_number = 1
    else:
        x2 = event.x
        y2 = event.y #Pega as coordendas do segundo ponto
        tela.create_line(x1, y1, x2, y2, width=4, fill="purple") #Desenha a linha
        e = CalcDist(x1, y1, x2, y2) #Calcula a distância
        real = comp_real/w * e
        print("Distancia em cm:", round(real, 2))
        tex.write(f'R {round(real, 2)*10}|')
        click_number = 0

        p1 = x2 - x1
        p2 = y2 - y1
        d = sqrt(p1 ** 2 + p2 ** 2)
        dados_reta.append([p1, p2, d])
        try:
            ang = CalcAngulo(dados_reta[-2][0],
                            dados_reta[-1][0],
                            dados_reta[-2][1],
                            dados_reta[-1][1],
                            dados_reta[-2][2],
                            dados_reta[-1][2])
            print("Ângulo da curva:", ang)
            if x1 < x2:
                print('Curva pra direita.\n')
                tex.write(f'D {round(ang,1)}|')
            else:
                print('Curva pra esquerda.\n')
                tex.write(f'E {round(ang,1)}|')
        except:
            print("Cálculo do ângulo requer duas linhas.\n")

def where(posn):
    cx=my_window.winfo_pointerx() - my_window.winfo_rootx()
    cy=my_window.winfo_pointery() - my_window.winfo_rooty()
    dx, dy = tela.coords(robot)
    tela.move(robot, (cx-dx)-(w_robo/2), (cy-dy)-(h_robo/2))


my_window = Tk()
my_window.title("Mapa da mesa")
my_window.config(cursor="cross")

photo = ImageTk.PhotoImage(Image.open("mesa.png")) #Mudar o caminho de acordo com a máquina.

w = photo.width()
h = photo.height()

roboCru = Image.open("robo.png")
roboCru = roboCru.resize((int(tam_robo * w / comp_real), int(tam_robo * w / comp_real)), Image.ANTIALIAS)
robo = ImageTk.PhotoImage(roboCru)

tela = Canvas(my_window, width=w, height=h, background='white')
tela.grid(row=0, column=0)

tela.create_image(0,0, image=photo, anchor='nw')

robot = tela.create_image(0,0, image=robo, anchor='nw')
w_robo = robo.width()
h_robo = robo.height()

tela.bind('<Button-1>', draw_line)
tela.bind('<Motion>', where)
click_number = 0

my_window.mainloop()
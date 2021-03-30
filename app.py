from tkinter import *
from math import sqrt, acos, degrees

dados_reta = []


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
        real = 200/w * e
        print("Distancia em cm:", round(real, 2))
        click_number = 0

        p1 = x2 - x1
        p2 = y2 - y1
        d = sqrt(p1 ** 2 + p2 ** 2)
        dados_reta.append([p1, p2, d])
        try:
            print("Ângulo da curva:", CalcAngulo(dados_reta[-2][0],
                                                 dados_reta[-1][0],
                                                 dados_reta[-2][1],
                                                 dados_reta[-1][1],
                                                 dados_reta[-2][2],
                                                 dados_reta[-1][2]), '\n')
        except:
            print("Cálculo do ângulo requer duas linhas.\n")


my_window = Tk()
my_window.title("Mapa da mesa")
my_window.config(cursor="cross")

photo = PhotoImage(file='C:\\Users\\Dell\\Downloads\\teste8.png') #Mudar o caminho de acordo com a máquina.

w = photo.width()
h = photo.height()

tela = Canvas(my_window, width=w, height=h, background='white')
tela.grid(row=0, column=0)

tela.create_image(0,0, image=photo, anchor='nw')
tela.bind('<Button-1>', draw_line)
click_number = 0

my_window.mainloop()

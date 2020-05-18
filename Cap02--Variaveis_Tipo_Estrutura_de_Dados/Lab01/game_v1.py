# Game Ping-Pong

#Importando alguns pacotes necessários
#tkinter é um api em python para criação de ambientes gráficos
from tkinter import * 
import random
import time

#Perguntando ao usuário qual nível de jogo ele deseja jogar
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))
#Variável length depende do nível que o jogador escolher jogar
length = 500/level

#root deve se referir à janela, ao ambiente gráfico
root = Tk() #abrindo janela?
root.title("Ping Pong") #Título da janela
root.resizable(0,0) #não é redimensionável
root.wm_attributes("-topmost", -1) #localização que aparece

#Dimensões da janela
# De acordo com estas dimensões, sabemos como a bolinha vai interagir com os limites da tela
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()

root.update()

# Variável
count = 0 
lost = False

#Criação da classe bola
class Bola:
	#Self seria a  própria bola?
	#canvas já foi definido
	#Barra é outra classe
	#color já é uma classe reconhecida pelo python
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color) #formato oval da bola
        self.canvas.move(self.id, 245, 200) #como a bola vai se mover

        starts_x = [-3, -2, -1, 1, 2, 3] #Onde a bola começa 
        random.shuffle(starts_x) #random start a partri do setpoint

        self.x = starts_x[0] #Coordenada x
        self.y = -3 #coordenada y

        self.canvas_height = self.canvas.winfo_height() #altura de que
        self.canvas_width = self.canvas.winfo_width() #largura de que


    def draw(self):
        self.canvas.move(self.id, self.x, self.y) 

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)


        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1 
                score() #Marcando pontos


        if pos[3] <= self.canvas_height: #condição de perda
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost 
            lost = True


class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color) #criação do retângulo da baarra
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left) #atribuindo os movimentos às setas
        self.canvas.bind_all("<KeyPress-Right>", self.move_right) 

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3


def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1) #delay para começar o jogo novamente
    Barra.draw() #Desenhar a barra
    Bola.draw() #Desenhar a bola


def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

def game_over():
    canvas.itemconfig(game, text="Game over!")


Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop() #repetição do loop
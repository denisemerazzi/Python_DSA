##Laboratório 01 - 03/04/2022
#Tarefa: Realizar o acréscimo de anotações sobre o código de desenvolvimento do jogo :-)

# Game Ping-Pong
# Importação da biblioteca Tkinter
from tkinter import 
import random
import time


#Criação da variável level e lenght: no level acrescenta-se o type inteiro e no lenght realiza-se uma divisão
#A variável recebe o valor digitado pelo usuário
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))
length = 500/level


#Instancia do objeto tk
root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

# Variável recebendo o resultado da função Canvas
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()
root.update()


# Variável
count = 0
lost = False

# Classe
class Bola:
    def __init__(self, canvas, Barra, color):
        
        #Variáveis
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        #Lista
        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        #Variáveis
        self.x = starts_x[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


# Utilização dos operadores condicionais (if, else)
    #Função self
    def draw(self):
        
        #Variáveis
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        #Condicional if
        if pos[1] <= 0:
            
            #Variável
            self.y = 3

          #Condicional if
        if pos[3] >= self.canvas_height:
            
            #Variável
            self.y = -3

          #Condicional if
        if pos[0] <= 0:
            
            #Variável
            self.x = 3
            
      #Condicional if   
    if pos[2] >= self.canvas_width:
            
            #Variável
            self.x = -3
        self.Barra_pos = self.canvas.coords(self.Barra.id)

      #Condicional if
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                
      # variáveis
                self.y = -3
                global count
                count +=1
                
                # Chamada à função
                score()

  #Condicional if/else
        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True

#Classe
class Barra:
    def __init__(self, canvas, color):
       
      #Variáveis
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

        #Função
    def draw(self):
        
         #Chamada ao método
        self.canvas.move(self.id, self.x, 0)

        #Variável
        self.pos = self.canvas.coords(self.id)

        #Condicional if
        if self.pos[0] <= 0:
            
             #Variável
            self.x = 0
        
        #Condicional if
        if self.pos[2] >= self.canvas_width:
            
            #Variável
            self.x = 0
        
        global lost
        
        #Condicional if
        if lost == False:
            self.canvas.after(10, self.draw)

            #Função
    def move_left(self, event):
        
        #Condicional if
        if self.pos[0] >= 0:
            self.x = -3

            #Função
    def move_right(self, event):
        
        #Condicional if
        if self.pos[2] <= self.canvas_width:
            self.x = 3

#Função
def start_game(event):
    
    #Variáveis
    global lost, count
    lost = False
    count = 0
    
    #Chamada à função
    score()
    
    # Variável que recebe o resultado da função
    canvas.itemconfig(game, text=" ")

    # Metodos dos objetos
    time.sleep(1)
    Barra.draw()
    Bola.draw()

#Função
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

    #Função
def game_over():
    canvas.itemconfig(game, text="Game over!")


# Instâncias dos objetos Barra e Bola
Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")

# Variáveis que recebem o resultado das funções
score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))
canvas.bind_all("<Button-1>", start_game)

# Executa o programa
root.mainloop()




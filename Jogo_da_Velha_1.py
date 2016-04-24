import tkinter as tk
from Jogo_da_Velha_parte2 import Jogo

class Tabuleiro:
    
    def __init__ (self): 
            
        self.window = tk.Tk()
        self.window.title("Jogo da Velha!")
        self.window.configure(height=64, width=42)
        
        self.meu_jogo = Jogo()
        
        self.botao1 = tk.Button(self.window)
        self.botao1.grid(row = 0, column = 0)
        self.botao1.configure(command = self.clicar1)
        self.botao1.configure(height=7, width=14)

        self.botao2 = tk.Button(self.window)
        self.botao2.grid(row = 0, column = 1)
        self.botao2.configure(command = self.clicar2)
        self.botao2.configure(height=7, width=14)

        self.botao3 = tk.Button(self.window)
        self.botao3.grid(row = 0, column = 2)
        self.botao3.configure(command = self.clicar3)
        self.botao3.configure(height=7, width=14)

        self.botao4 = tk.Button(self.window)
        self.botao4.grid(row = 1, column = 0)
        self.botao4.configure(command = self.clicar4)
        self.botao4.configure(height=7, width=14)

        self.botao5 = tk.Button(self.window)
        self.botao5.grid(row = 1, column = 1)
        self.botao5.configure(command = self.clicar5)
        self.botao5.configure(height=7, width=14)

        self.botao6 = tk.Button(self.window)
        self.botao6.grid(row = 1, column = 2)
        self.botao6.configure(command = self.clicar6)
        self.botao6.configure(height=7, width=14)

        self.botao7 = tk.Button(self.window)
        self.botao7.grid(row = 2, column = 0)
        self.botao7.configure(command = self.clicar7)
        self.botao7.configure(height=7, width=14)

        self.botao8 = tk.Button(self.window)
        self.botao8.grid(row = 2, column = 1)
        self.botao8.configure(command = self.clicar8)
        self.botao8.configure(height=7, width=14)

        self.botao9 = tk.Button(self.window)
        self.botao9.grid(row = 2, column = 2)
        self.botao9.configure(command = self.clicar9)
        self.botao9.configure(height=7, width=14)
        
        self.label = tk.Label(self.window, text = "Próxima jogada: X")
        self.label.grid(row = 3)
        self.label.configure(height=1)
        
    def clicar1 (self):
        self.meu_jogo.recebe_jogada(0, 0)
        self.meu_jogo.jogador
        if self.meu_jogo.jogador == 1:
            self.botao9.configure(text="X")
        else:
            self.botao9.configure(text="O")
        self.mudar_Label()
        self.verifica()
        
    def clicar2 (self):
        self.meu_jogo.recebe_jogada(0, 1)
        self.meu_jogo.jogador
        if self.meu_jogo.jogador == 1:
            self.botao9.configure(text="X")
        else:
            self.botao9.configure(text="O")
        self.mudar_Label()
        self.verifica()
        
    def clicar3 (self):
        self.meu_jogo.recebe_jogada(0, 2)
        self.meu_jogo.jogador
        if self.meu_jogo.jogador == 1:
            self.botao9.configure(text="X")
        else:
            self.botao9.configure(text="O")
        self.mudar_Label()
        self.verifica()
        
    def clicar4 (self):
        self.meu_jogo.recebe_jogada(1, 0)
        self.meu_jogo.jogador
        if self.meu_jogo.jogador == 1:
            self.botao9.configure(text="X")
        else:
            self.botao9.configure(text="O")
        self.mudar_Label()
        self.verifica()
        
    def clicar5 (self):
        self.meu_jogo.recebe_jogada(1, 1)
        self.meu_jogo.jogador
        if self.meu_jogo.jogador == 1:
            self.botao9.configure(text="X")
        else:
            self.botao9.configure(text="O")
        self.mudar_Label()
        self.verifica()
        
    def clicar6 (self):
        self.meu_jogo.recebe_jogada(1, 2)
        self.meu_jogo.jogador
        if self.meu_jogo.jogador == 1:
            self.botao9.configure(text="X")
        else:
            self.botao9.configure(text="O")
        self.mudar_Label()
        self.verifica()
        
    def clicar7 (self):
        self.meu_jogo.recebe_jogada(2, 0)
        self.meu_jogo.jogador
        if self.meu_jogo.jogador == 1:
            self.botao9.configure(text="X")
        else:
            self.botao9.configure(text="O")
        self.mudar_Label()
        self.verifica()
        
    def clicar8 (self):
        self.meu_jogo.recebe_jogada(2, 1)
        self.meu_jogo.jogador
        if self.meu_jogo.jogador == 1:
            self.botao9.configure(text="X")
        else:
            self.botao9.configure(text="O")
        self.mudar_Label()
        self.verifica()
        
    def clicar9 (self):
        self.meu_jogo.recebe_jogada(2, 2)
        self.meu_jogo.jogador 
        if self.meu_jogo.jogador == 1:
            self.botao9.configure(text="X")
        else:
            self.botao9.configure(text="O")
        self.mudar_Label()
        self.verifica()
        
    def verifica(self):
        self.meu_jogo.verifica_ganhador()
        if self.meu_jogo.verifica_ganhador == (1 or 2 or 0):
            self.meu_jogo.limpa_jogada()
        else:
            return -1
            
    def mudar_Label(self):
        if self.label["text"] == ("Próxima jogada: X"):
            self.label["text"] == ("Próxima jogada: O")
        elif self.label["text"] == ("Próxima jogada: O"):
            self.label["text"] == ("Próxima jogada: X")       
            
    def iniciar(self):
        self.window.mainloop() 

jogo = Tabuleiro()
jogo.iniciar()
            
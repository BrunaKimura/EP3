import tkinter as tk

class Tabuleiro:
    
    def __init__ (self): 
            
        self.window = tk.Tk()
        self.window.title("Jogo da Velha!")
        self.window.configure(height=64, width=42)
        
        self.meu_jogo = Jogo 
        
        botao1 = tk.Button(self.window)
        botao1.grid(row = 0, column = 0)
        botao1.configure(command = self.meu_jogo.recebe_jogada(self, 0, 0))
        botao1.configure(height=7, width=14)

        botao2 = tk.Button(self.window)
        botao2.grid(row = 0, column = 1)
        botao2.configure(command = self.meu_jogo.recebe_jogada(self, 0, 1))
        botao2.configure(height=7, width=14)

        botao3 = tk.Button(self.window)
        botao3.grid(row = 0, column = 2)
        botao3.configure(command = self.meu_jogo.recebe_jogada(self, 0, 2))
        botao3.configure(height=7, width=14)

        botao4 = tk.Button(self.window)
        botao4.grid(row = 1, column = 0)
        botao4.configure(command = self.meu_jogo.recebe_jogada(self, 1, 0))
        botao4.configure(height=7, width=14)

        botao5 = tk.Button(self.window)
        botao5.grid(row = 1, column = 1)
        botao5.configure(command = self.meu_jogo.recebe_jogada(self, 1, 1))
        botao5.configure(height=7, width=14)

        botao6 = tk.Button(self.window)
        botao6.grid(row = 1, column = 2)
        botao6.configure(command = self.meu_jogo.recebe_jogada(self, 1, 2))
        botao6.configure(height=7, width=14)

        botao7 = tk.Button(self.window)
        botao7.grid(row = 2, column = 0)
        botao7.configure(command = self.meu_jogo.recebe_jogada(self, 2, 0))
        botao7.configure(height=7, width=14)

        botao8 = tk.Button(self.window)
        botao8.grid(row = 2, column = 1)
        botao8.configure(command = self.meu_jogo.recebe_jogada(self, 2, 1))
        botao8.configure(height=7, width=14)

        botao9 = tk.Button(self.window)
        botao9.grid(row = 2, column = 2)
        botao9.configure(command = self.meu_jogo.recebe_jogada(self, 2, 2))
        botao9.configure(height=7, width=14)
        
        label = tk.Label(self.window, text = "Próxima jogada:")
        label.grid(row = 3)
        label.configure(height=1)
        
    def iniciar(self):
        self.window.mainloop() 

jogo = Tabuleiro()
jogo.iniciar()
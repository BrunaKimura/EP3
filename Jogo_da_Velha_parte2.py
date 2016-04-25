class Jogo:

#Criação de um jogador e de uma tabela feita de por uma lista e três sublistas.
    def __init__ (self):
        self.jogador = 2
        self.A = [[0,0,0], [0,0,0], [0,0,0]]

#Esta def rece o local onde foi feita a jogada e o jogador que a fez.        
    def recebe_jogada(self, linha, coluna):
        if self.A[linha][coluna] == 0:        
            self.A[linha][coluna]= self.jogador
        
        if self.jogador == 1:
            self.jogador = 2
        else:
            self.jogador = 1
            
    def verifica_ganhador(self):
        #todos os modos possíveis de ganhar o jogo.
        horizontal1 = self.A[0][0]==self.A[0][1] and self.A[0][0]==self.A[0][2]
        horizontal2 = self.A[1][0]==self.A[1][1] and self.A[1][0]==self.A[1][2]
        horizontal3 = self.A[2][0]==self.A[2][1] and self.A[2][0]==self.A[2][2]
        
        vertical1 = self.A[0][0]==self.A[1][0] and self.A[0][0]==self.A[2][0]
        vertical2 = self.A[0][1]==self.A[1][1] and self.A[0][1]==self.A[2][1]
        vertical3 = self.A[0][2]==self.A[1][2] and self.A[0][2]==self.A[2][2]
        
        diagonal1 = self.A[0][0]==self.A[1][1] and self.A[0][0]==self.A[2][2]
        diagonal2 = self.A[0][2]==self.A[0][1] and self.A[0][2]==self.A[2][0]
        
        #Conferir quem ganhou o jogo.
        if horizontal1 or horizontal2 or horizontal3 or vertical1 or vertical2 or vertical3 or diagonal1 or diagonal2 == 1:
            return 1
        elif horizontal1 or horizontal2 or horizontal3 or vertical1 or vertical2 or vertical3 or diagonal1 or diagonal2 == 2:
            return 2
        #Neste caso deu velha, ou seja, empate!
        elif (horizontal1 or horizontal2 or horizontal3 or vertical1 or vertical2 or vertical3 or diagonal1 or diagonal2) != (1 and 2):
            return 0 
        #neste caso o jogo não acabou!
        else:
            return -1
   #limpa o tabuleiro de lista e sublista!         
    def limpa_jogada(self):
        self.tabuleiro = [[0,0,0], [0,0,0], [0,0,0]]

class Jogo:

#Criação de um jogador e de uma tabela feita de por uma lista e três sublistas.
    def __init__ (self):
        self.jogador = 1
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
        
        if (self.A[0][0]==self.A[0][1] and self.A[0][0]==self.A[0][2] and self.A[0][0]==1 or
        self.A[1][0]==self.A[1][1] and self.A[1][0]==self.A[1][2] and self.A[1][0]==1 or
        self.A[2][0]==self.A[2][1] and self.A[2][0]==self.A[2][2] and self.A[2][0]==1 or
        self.A[0][0]==self.A[1][0] and self.A[0][0]==self.A[2][0] and self.A[0][0]==1 or
        self.A[0][1]==self.A[1][1] and self.A[0][1]==self.A[2][1] and self.A[0][1]==1 or
        self.A[0][2]==self.A[1][2] and self.A[0][2]==self.A[2][2] and self.A[0][2]==1 or
        self.A[0][0]==self.A[1][1] and self.A[0][0]==self.A[2][2] and self.A[0][0]==1 or
        self.A[0][2]==self.A[1][1] and self.A[0][2]==self.A[2][0] and self.A[0][2]==1):
               return 1
            
        if (self.A[0][0]==self.A[0][1] and self.A[0][0]==self.A[0][2] and self.A[0][0]==2 or
        self.A[1][0]==self.A[1][1] and self.A[1][0]==self.A[1][2] and self.A[1][0]==2 or
        self.A[2][0]==self.A[2][1] and self.A[2][0]==self.A[2][2] and self.A[2][0]==2 or
        self.A[0][0]==self.A[1][0] and self.A[0][0]==self.A[2][0] and self.A[0][0]==2 or
        self.A[0][1]==self.A[1][1] and self.A[0][1]==self.A[2][1] and self.A[0][1]==2 or
        self.A[0][2]==self.A[1][2] and self.A[0][2]==self.A[2][2] and self.A[0][2]==2 or
        self.A[0][0]==self.A[1][1] and self.A[0][0]==self.A[2][2] and self.A[0][0]==2 or
        self.A[0][2]==self.A[1][1] and self.A[0][2]==self.A[2][0] and self.A[0][2]==2):
            return 2
        
        #Neste caso deu velha, ou seja, empate!
        elif self.A[0][0]!=0 and self.A[0][1]!=0 and self.A[0][2]!=0 and self.A[1][0]!=0 and self.A[1][1]!=0 and self.A[1][2]!=0 and self.A[2][0]!=0 and self.A[2][1]!=0 and self.A[2][2]!=0:
            return 0
          
        #neste caso o jogo não acabou!
        else:
            return -1


   #limpa o tabuleiro de lista e sublista!         
    def limpa_jogada(self):
        self.A = [[0,0,0], [0,0,0], [0,0,0]]

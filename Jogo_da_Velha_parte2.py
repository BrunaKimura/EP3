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
         #todos modos possíveis de ganhar e as condições para saber se foi o jogador 1 ou 2 quem ganhou!
        if self.A[0][0]==self.A[0][1] and self.A[0][0]==self.A[0][2]:
            if self.A[0][0]==1:
                return 1
            elif self.A[0][0]==2:
                return 2
        elif self.A[1][0]==self.A[1][1] and self.A[1][0]==self.A[1][2]:
            if self.A[1][0]==1:
                return 1
            elif self.A[1][0]==2:
                return 2
        elif self.A[2][0]==self.A[2][1] and self.A[2][0]==self.A[2][2]:
            if self.A[2][0]==1:
                return 1
            elif self.A[2][0]==2:
                return 2
        
        if self.A[0][0]==self.A[1][0] and self.A[0][0]==self.A[2][0]:
            if self.A[0][0]==1:
                return 1
            elif self.A[0][0]==2:
                return 2
        if self.A[0][1]==self.A[1][1] and self.A[0][1]==self.A[2][1]:
            if self.A[0][1]==1:
                return 1
            elif self.A[0][1]==2:
                return 2
        if self.A[0][2]==self.A[1][2] and self.A[0][2]==self.A[2][2]:
            if self.A[0][2]==1:
                return 1
            elif self.A[0][2]==2:
                return 2
        
        if self.A[0][0]==self.A[1][1] and self.A[0][0]==self.A[2][2]:
            if self.A[0][0]==1:
                return 1
            elif if self.A[0][0]==2:
                return 2
        if self.A[0][2]==self.A[0][1] and self.A[0][2]==self.A[2][0]:
            if self.A[0][2]==1:
                return 1
            elif self.A[0][2]==2:
                return 2
        
        #Conferir quem ganhou o jogo.
        if (self.horizontal1 or self.horizontal2 or self.horizontal3 or self.vertical1 or self.vertical2 or self.vertical3 or self.diagonal1 or self.diagonal2) == (1):
            return 1
        elif (self.horizontal1 or self.horizontal2 or self.horizontal3 or self.vertical1 or self.vertical2 or self.vertical3 or self.diagonal1 or self.diagonal2) == (2):
            return 2
        #Neste caso deu velha, ou seja, empate!
        elif (self.horizontal1 or self.horizontal2 or self.horizontal3 or self.vertical1 or self.vertical2 or self.vertical3 or self.diagonal1 or self.diagonal2) != (1 and 2):
            return 0 
        #neste caso o jogo não acabou!
        else:
            return -1
   
   
   #limpa o tabuleiro de lista e sublista!         
    def limpa_jogada(self):
        self.tabuleiro = [[0,0,0], [0,0,0], [0,0,0]]

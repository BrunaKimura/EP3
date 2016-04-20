class Jogo:

    def __init__ (self):
        self.jogador = 1
        self.A = [[0,0,0], [0,0,0], [0,0,0]]
        
    def recebe_jogada(self, linha, coluna):
        self.A[linha][coluna]= self.jogador
        if self.jogador == 1:
            self.jogador == 2
        else:
            self.jogador == 2
            
    def verifica_ganhador(self):
        horizontal1 = self.A[0][0]==self.A[0][1]==self.A[0][2]
        horizontal2 = self.A[1][0]==self.A[1][1]==self.A[1][2]
        horizontal3 = self.A[2][0]==self.A[2][1]==self.A[2][2]
        
        vertical1 = self.A[0][0]==self.A[1][0]==self.A[2][0]
        vertical2 = self.A[0][1]==self.A[1][1]==self.A[2][1]
        vertical3 = self.A[0][2]==self.A[1][2]==self.A[2][2]
        
        diagonal1 = self.A[0][0]==self.A[1][1]==self.A[2][2]
        diagonal2 = self.A[0][2]==self.A[0][1]==self.A[2][0]
        
        if horizontal1 or horizontal2 or horizontal3 or vertical1 or vertical2 or vertical3 or diagonal1 or diagonal2 == 1:
            return 1
        elif horizontal1 or horizontal2 or horizontal3 or vertical1 or vertical2 or vertical3 or diagonal1 or diagonal2 == 2:
            return 2
        elif (horizontal1 or horizontal2 or horizontal3 or vertical1 or vertical2 or vertical3 or diagonal1 or diagonal2) != (1 and 2):
            return 0 
        else:
            return -1
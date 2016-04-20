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
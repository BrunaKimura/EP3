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
        if self.A[0][0]==self.A[0][1] and self.A[0][0]==self.A[0][2] and self.A[0][0]==1:
            return 1

        #neste caso o jogo não acabou!
        else:
            return -1
   #limpa o tabuleiro de lista e sublista!         
    def limpa_jogada(self):
        self.tabuleiro = [[0,0,0], [0,0,0], [0,0,0]]

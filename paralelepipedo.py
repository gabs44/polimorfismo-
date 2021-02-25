from forma3D import Forma3D as P
import math

class Paralelepipedo(P):
    def __init__(self, comprimento, largura, altura):
        self.comprimento = comprimento
        self.largura = largura
        self.altura = altura
    
    def volume(self):
        return self.comprimento * self.largura * self.altura
    
    def diagonal(self):
        return math.sqrt(self.comprimento**2 + self.largura**2 + self.altura**2)

    def descricao(self):
        return 'paralelepípedo'
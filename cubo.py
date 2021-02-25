from forma3D import Forma3D as C
import math

class Cubo(C):
    def __init__(self, lado):
        self.lado = lado

    def volume(self):
        return self.lado **3

    def diagonal(self):
        return self.lado * math.sqrt(3) #raiz de 3

    def descricao(self):
        return 'cubo'
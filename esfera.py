from forma3D import Forma3D as E
import math

class Esfera(E):
    def __init__(self, raio):
        self.raio = raio

    def volume(self):
        return 4/3 * math.pi * self.raio**3

    def descricao(self):
        return 'esfera'

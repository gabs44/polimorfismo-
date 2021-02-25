from FormaPlana import FormaPlana as Q

class Quadrado(Q):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.lado * 4

    def diagonal(self):
        return self.lado * 1.414 #valor da raiz de 2

    def descricao(self):
        return ' quadrado'



from cubo import Cubo as C
from paralelepipedo import Paralelepipedo as P
from esfera import Esfera as E

c1 = C(3)
p1 = P(2, 3, 4)
e1 = E(2)


print(f' O volume do {c1.descricao()} é igual a {c1.volume()} cm3')
print(f' A diagonal do {c1.descricao()} é igual a {c1.diagonal()} cm')
print()
print(f' O volume do {p1.descricao()} é igual a {p1.volume()} cm3')
print(f' A diagonal do {p1.descricao()} é igual a {p1.diagonal()} cm')
print()
print(f' O volume da {e1.descricao()} é igual a {e1.volume()} cm2')


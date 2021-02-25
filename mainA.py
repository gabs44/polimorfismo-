from quadrado import Quadrado as Q
from retangulo import Retangulo as R
from circulo import Circulo as C


c1 = C(2)
r1 = R(2, 3)
q1 = Q(3)


print(f' A área do {q1.descricao()} é igual a {q1.area()} cm2')
print(f' O perímetro do {q1.descricao()} é igual a {q1.perimetro()} cm')
print(f' A diagonal do {q1.descricao()} é igual a {q1.diagonal()} cm')
print()
print(f' A área do {r1.descricao()} é igual a {r1.area()} cm2')
print(f' O perímetro do {r1.descricao()} é igual a {r1.perimetro()} cm')
print(f' A diagonal do {r1.descricao()} é igual a {r1.diagonal()} cm')
print()
print(f' A área do {c1.descricao()} é igual a {c1.area()} cm2')
print(f' O perímetro do {c1.descricao()} é igual a {c1.perimetro()} cm')



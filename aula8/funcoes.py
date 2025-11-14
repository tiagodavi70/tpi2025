from funcoesoutroficheiro import eq1grau

def soma(a, b):
    return a + b

def eq2grau(x, a, b, c=0):
    return (a * x*x) + (b * x) + c

num1 = 1
num2 = 2

c = soma(num1, num2)
print(c)

print(soma(num2, num1))

resultado = eq2grau(2, 3, 4, 5)
print(resultado)

# r = funcoesoutroficheiro.eq1grau(2,3)
# print(r)

r = eq1grau(2,3)
print(r)

from random import randint

randint(1, 4)
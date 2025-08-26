import math

# INTRODUÇÃO
print("!!Olá, seja bem-vindo a Calculadora de equação de segundo Grau!!")

# Local para inserir os valores de (a, b, c)
a = float(input("Por favor digite o Valor de A:"))
b = float(input("Por favordigite o valor de B:"))
c = float(input("Por favor digite o valor de C:"))

# Local para calcular o DELTA
delta = b**2 - 4*a*c

# Local para discernir se tem como fazer o cálculo
if delta < 0:
    print("Essa equação não possui raízes reais")
elif delta == 0:
    x = -b / (2 * a)
    print(f"A raiz é única: {x}")
else: # Local que calcula e retorna os valores de X1 e X2 da equação
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"O RESULTADO É: {x1} e {x2}")

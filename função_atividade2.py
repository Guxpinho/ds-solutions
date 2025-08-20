import math

def formula_de_bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Não existem raízes reais"
    elif delta == 0:
        x = -b / (2 * a)
        return x
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        return x1, x2

def area_quadrado(b, h):
    area = b * h
    return area

def volume_do_cubo(a):
    volume = a ** 3
    return volume

def menu_opcao():
        print('Bem-vindo à calculadora\n')
        print('\n')
        print('+-----------------------------------+')
        print('| Código | Operação                 |')
        print('+-----------------------------------+')
        print('|   1    | calcular bhaskara        |')
        print('|   2    | calcular área do quadrado|')
        print('|   3    | calcular o volume do cubo|')
        print('|   4    | sair                     |')
        print('+-----------------------------------+')
        escolha = int(input("escolha uma dessas opções: "))
        return escolha
        
while True:
    escolha = menu_opcao()        
            
    if escolha == 1:
        a = float(input("digite o valor de a: "))
        b = float(input("digite o valor de b: "))
        c = float(input("digite o valor de c: "))
        print(F"o valor da formala de bhaskara = {formula_de_bhaskara(a, b, c)}")
    elif escolha == 2:
        a = float(input("digite o valor de a: "))
        b = float(input("digite o valor de b: "))
        print(F"o valor da área do quadrado é  = {area_quadrado(a, b)}")
    elif escolha == 3:
        a = float(input("digite o valor do volume de cubo a: "))
        print(F"o valor do volume do cubo é = {volume_do_cubo(a)}")
    elif escolha == 4:
        break
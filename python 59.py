
def soma(n1, n2):
    soma = n1 +n2
    return soma

def subtracao(n1,n2):
    sub = n1 - n2
    return sub

def multiplicacao(n1,n2):
    mult = n1 * n2
    return mult

def divisao(n1,n2):
    div = n1/ n2
    return div

def resto_de_divisao(n1, n2):
    resto = n1 % n2
    return resto

def valor_inteiro_da_divisao(n1, n2):
    valor_inteiro = n1 // n2
    return valor_inteiro

def raiz_quadrada(n1):
    return n1 ** 0.5

def exponencial(n1, n2):
    expo = n1 ** n2
    return expo

num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
print('Bem-vindo à calculadora\n')
print('\n')
print('+------------------------------+')
print('| Código | Operação             |')
print('+------------------------------+')
print('|   1    | Soma                |')
print('|   2    | Subtração           |')
print('|   3    | Multiplicação       |')
print('|   4    | Divisão             |')
print('|   5    | Resto da Divisão    |')
print('|   6    | Valor Inteiro Divisão|')
print('|   7    | Raiz Quadrada       |')
print('|   8    | Exponencial         |')
print('+------------------------------+')

escolha = int(input("escolha uma dessas opções: "))
if escolha == 1:
    print(F"o valor da soma {num1} + {num2} = {soma(num1, num2)}")
elif escolha == 2:
    print(F"o valor da subtração {num1} + {num2} = {subtracao(num1, num2)}")
elif escolha == 3:
    print(F"o valor da multiplicação {num1} * {num2} = {multiplicacao(num1, num2)}")
elif escolha == 4:
    print(F"o valor da divisão {num1} / {num2} = {divisao(num1, num2)}")
elif escolha == 5:
    print(F"o valor da resto da divisão {num1} dividido  {num2} = {resto_de_divisao(num1, num2)}")
elif escolha == 6 :
    print(F"o valor da valor inteiro da divisão{num1} // {num2} = {valor_inteiro_da_divisao(num1, num2)}")
elif escolha == 7:
    print(F"o valor da raiz quadrada{num1} **  = {raiz_quadrada(num1)}")
elif escolha == 8:
     print(F"o valor da exponencial {num1} ** {num2} = {exponencial(num1, num2)}")
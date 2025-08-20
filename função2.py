def soma(n1, n2):
    soma = n1 +n2
    return soma

def subtracao(n1,n2):
    sub = n1 - n2
    return sub

print('bem vindo a calculadora')
num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
op = int(input("digite 1 para somar e 2 para subtrair"))
if op == 1:
    print(F"o valor da soma {num1} + {num2} = {soma(num1, num2)}")
elif op == 2:
    print(F"o valor da subtração {num1} + {num2} = {subtracao(num1, num2)}")
else: 
    print ('comando invalido!!')
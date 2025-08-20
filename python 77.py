i = 0
lista = []

print("---QUADRADO DE UM NUMERO QUALQUER---")
while True:
    numero = int(input("escolha um numero (se quiser encerrar digite 0): "))
    i += 1
    if numero == 0:
        break
    quadrado = numero**2
    lista.append(quadrado)
    somam =  sum(lista)
print(f"\n Essa é sua lista: {lista}, e essa é sua soma total do quadrado de cada numero: {somam}")


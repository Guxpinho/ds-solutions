
numeros = []
while True:
    num = int(input("Digite o número da primeira lista (0 para sair): "))
    if num == 0:
        break
    numeros.append(num)
numeros.sort()
print(f"Essa é a ordem dos seus números: {numeros}")


sem_repetidos = list(set(numeros))
sem_repetidos.sort()
print(f"Números sem repetições: {sem_repetidos}")


repetidos = []
for n in sem_repetidos:
    if numeros.count(n) > 1:
        repetidos.append(n)
print(f"Números que se repetem: {repetidos}")


if not repetidos:
    print("Essa lista não se repete em nenhum número.")
else:
    print("Essa lista possui números repetidos.")


    
    


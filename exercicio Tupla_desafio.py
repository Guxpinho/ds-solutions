lista_original = []
lista_par = []
lista_impar = []

while True:
    num = int(input("Digite o número da primeira lista (0 para sair): "))
    if num == 0:
        break
    else:
        lista_original.append(num)

lista_original.sort()
print("Lista original ordenada:", lista_original)

for num in lista_original:
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)


soma = 0
for n in lista_original:
    soma += n

print("Lista de números ímpares:", lista_impar)
print("Lista de números pares:", lista_par)
print("Soma total dos números:", soma)

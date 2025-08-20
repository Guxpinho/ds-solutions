lista_digite = []
lista_pares = []
lista_impares = []

def verificar_par_ou_impar(lista):
    for num in lista:
        if num % 2 == 0:
            lista_pares.append(num)
            lista_pares.sort
        else:
            lista_impares.append(num)
            lista_impares.sort
print("-----NUMEROS PARES E IMPARES-----")
while True:
    digite = int(input("Digite qualquer número. Se quiser sair digite (-1): "))
    if digite == -1:
        break
    lista_digite.append(digite)
    lista_digite.sort

verificar_par_ou_impar(lista_digite)
print(F"Esses são todos os numeros da lista: {lista_digite}")
print(f"Esses são seus números pares: {lista_pares}")
print(f"Esses são seus números ímpares: {lista_impares}")

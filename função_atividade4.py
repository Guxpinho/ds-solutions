lista_digite = []
def vogais(digite):
    contador = 0 
    for letras in digite:
     if letras in ('a, e, i, o, u'):
       contador += 1
    return contador
print("-----VOGAIS DA FRASE-----")
digite = input("digite uma frase:").lower()
lista_digite.append(digite)
print(F"Essas são suas vogais: {vogais(digite)}") 
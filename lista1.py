lista = [4, 5, 3, 5]
print(f"lista inicial:_{lista}")
lista.append(2)
print(f"{lista}") #adiciona numero 2 a lista
lista.insert(2,-3)
print(f"{lista}") # adicione o numero -3 da posição 2 da lista
lista.remove(4)
print(f"{lista}") # remove o numero 4
lista.sort()
print(f"{lista}") #organiza a lista por ordem crescente 
lista.reverse()
print(f"{lista}") #inverte a lista
qnt = lista.count(5) #conta a quantidade de numeros selecionados
print(F"{qnt}")
exc = lista.pop() #remover o ultimo item da lista 
print(f"{lista}")
print(exc)
del lista[2] #deleta o numero 2 da lista
print(F"{lista}")
del lista[2:5] #deleta de 2 a 5
print(F"{lista}")
lista.clear()
print(F"{lista}")

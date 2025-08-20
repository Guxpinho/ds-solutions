import random

print("-------Fazer um sorteio de Nomes--------")
nova_lista = []
lista_da_escolha = []
while True:
    nomes = input("Digite algum nome (se quiser parar digite 0): ").lower()
    if nomes == '0':
        break
    nova_lista.append(nomes)
print(f"Essa é a lista de pessoas: {nova_lista}")

while True:
    if not nova_lista:
        print("Todos os nomes foram sorteados")
        break
    escolha = random.choice(nova_lista)
    print(f"Nome sortido = {escolha}")

    nova_lista.remove(escolha)
    lista_da_escolha.append(escolha)
    
    print(F"Essa é sua lista nova: {lista_da_escolha}")
    
    lista_da_escolha.sort()
    print(f"Essa é sua lista em ordem alfabética:")



    
    
    

    
    


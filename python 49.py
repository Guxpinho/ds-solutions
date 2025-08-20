nova= []
soma = 0 
mut = 1 
while True:
    numeros_aleatorios = int(input(f"digite um numero: "))
    if numeros_aleatorios == 0:
        print("Fim da lista")
        break
    soma += numeros_aleatorios
    mut *= numeros_aleatorios
    nova.sort()
    print(f"{nova}")
    print(F"{soma}")
    print(F"{mut}") 
       
    
        

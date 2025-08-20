# Lists to store grades and their corresponding weights
lista_notas = []
lista_pesos = []

def media_ponderada(notas, pesos):
    # Variables to store weighted sum and sum of weights
    total_ponderado = 0
    total_pesos = 0
    
    # Loop through each grade and weight
    for i in range(len(notas)):
        nota_atual = notas[i]
        peso_atual = pesos[i]
        
        # Multiply grade by its weight and add to total
        total_ponderado += nota_atual * peso_atual
        total_pesos += peso_atual
    
    # Avoid division by zero
    if total_pesos == 0:
        return 0
    
    # Return weighted average
    return total_ponderado / total_pesos

# Loop to collect grades and weights
while True:
    nota = float(input("Qual é sua nota? Digite 0 para sair: "))
    if nota == 0:
        break
    peso = float(input("Qual é o peso dessa nota? "))
    lista_notas.append(nota)
    lista_pesos.append(peso)

# Display results
print(f"Essas são suas notas: {lista_notas}")
print(f"E esses são os pesos das suas notas: {lista_pesos}")
print(f"Essa é a média ponderada das notas: {media_ponderada(lista_notas, lista_pesos):.2f}")

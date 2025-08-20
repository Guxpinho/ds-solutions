import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

print("---Vou treinar você para a tabuada---")
acertou = 0
errou = 0

numero = int(input("Que número você deseja treinar: "))

for repeticao in range(1, 11):
    limpar_tela()  
    print(f"Tabuada do {numero} - Pergunta {repeticao} de 10")
    resultado = int(input(f"{numero} * {repeticao} = "))
    resultado_certo = numero * repeticao
    if resultado == resultado_certo:
        print("Correto")
        acertou += 1
    else:
        print(f"Errou, que pena! O valor correto é {resultado_certo}")
        errou += 1
    
    print(f"Total de acertos até agora: {acertou}")
    print(f"Total de erros até agora: {errou}")
    input("escreva qualquer coisa para continuar: ")

limpar_tela()
print(f"Fim do treino! Você acertou {acertou} vezes e errou {errou} vezes.")

   
    

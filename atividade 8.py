def fatorial(n):
    # Initialize result as 1
    resultado = 1
    # Multiply result by each number from 2 to n
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Infinite loop until user decides to exit
while True:
    numero = int(input("Digite um número inteiro positivo: "))

    # Check if the number is negative
    if numero < 0:
        print("O numero não está certo! Digite um número inteiro positivo.")
    else:
        # Show factorial result
        print(f"O fatorial de {numero} é {fatorial(numero)}")
        
        # Ask if the user wants to exit
        saida = input("Caso queira sair, selecione (X) ou escreva qualquer coisa para continuar: ")
        if saida.strip().lower() == 'x':
            print("Saindo do programa.")
            break

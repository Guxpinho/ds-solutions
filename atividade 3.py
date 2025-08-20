def valores_inteiros():
    # Explain what the program will do
    print("---vou encotrar seu maior, menor e a média dos números lidos---")

    # Variables to store max, min, and sum
    maior = 0
    menor = 0
    soma = 0

    # Loop to read 10 numbers
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        soma += numero  # Add to the total sum

        # Update largest number found
        if maior is 0 or numero > maior:
            maior = numero
        # Update smallest number found
        if menor is 0 or numero < menor:
            menor = numero

    # Calculate the average
    media = soma / 10

    # Display results
    print(f"Esse é seu maior valor:{maior}")
    print(f"Esse é seu menor valor:{menor}")
    print(f"esse é sua média: {media:.2f}")

# Execute the function
valores_inteiros()

        

    

    
    


def verificar_numeros_primos():
    # Inform the user about the program
    print("---verificar se o número é primo ou não---")
    
    # Get number input from the user
    numero = int(input("Digite um número de 1 a 100: "))
    
    # Predefined list of prime numbers between 1 and 100
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    # Check if the number is in the prime list
    if numero in primos:
        print("Seu número é primo")
    else:
        print("São números normais")  # Not a prime number
        
def mostrar_numero_primo():
    # Store prime numbers found
    primos = ''
    
    # Loop through numbers from 2 to 99
    for numero in range (2,100,1):
        numero_primo = True  # Assume number is prime
        
        # Check for divisors
        for i in range (2, numero -1, 1):
            if (numero % i) == 0:
                numero_primo = False
                break
        
        # If prime, add to the string
        if numero_primo:
            primos = primos + str(numero) + "-"
    
    # Display prime numbers found
    print(f"Número primos de 1 a 100: {primos}")

# Run both functions
verificar_numeros_primos()
mostrar_numero_primo()

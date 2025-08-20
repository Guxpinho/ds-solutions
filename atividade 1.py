def caracter_da_letra():
    # Display message explaining the program's purpose
    print("--vou verificar se sua letra é vogal, consoante ou símbolo--")
    
    # Ask the user for input and convert it to lowercase
    letra = input("digite qualquer coisa: ").lower()
    
    # Check if the input is a vowel
    if letra in "aeiou":
        print("vogal")  # It's a vowel
    # Check if the input is a consonant
    elif letra in "bcdfghjklmnpqrstvwxyz":
        print("consoante")  # It's a consonant
    # If it's neither a vowel nor a consonant, it's a symbol
    else: 
        print("símbolo")
        
# Call the function to execute the program
caracter_da_letra()

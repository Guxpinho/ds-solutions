# Ask for the user's name
nome = input("Qual é seu nome: ").lower()

# Infinite loop until user chooses to exit
while True:
    # Ask for password
    senha = input ("Qual é sua senha: ").lower()
    
    # Check if the password is the same as the name
    if senha == nome:
        print("*erro* digite novamente sua senha. ")
    else:
        print("Obrigado por contribuir com nossa pesquisa.")
    
    # Ask if the user wants to exit
    saida = input("Caso queira sair, selecione (X) ou escreva qualquer coisa para continuar: ")
    if saida.strip().lower() == "x":
            print("Saindo do programa.")
            break



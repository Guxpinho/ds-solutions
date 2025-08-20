import os

def limpar_tela():
    # Clear terminal screen (Windows or Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---Vou verificar se essas pessoas estão com febre ou não---")

def ler_numero_pessoas():
    # Read the number of people to be analyzed
    while True:
            numero = int(input("Número de pessoas que serão analisadas: "))
            if numero > 0:
                return numero
            else:
                print("Por favor, digite um número inteiro maior que zero.")

# Clear the screen and show intro message
limpar_tela()

# Counters for different temperature categories
qntd_normal = 0
qntd_febril = 0
qntd_febre = 0
qntd_febre_alta = 0
qntd_mortas = 0
pessoas = 0
soma_temperaturas = 0

# Get total number of people to check
numero_temp = ler_numero_pessoas()

# Loop through each person
while pessoas < numero_temp:
    try:
        n = float(input(f"Digite a temperatura {pessoas + 1}º número: "))
    except ValueError:
        print("Entrada inválida. Digite um número válido para a temperatura.")
        continue  

    pessoas += 1
    soma_temperaturas += n

    # Classify temperature readings
    if n < 25:
        qntd_mortas += 1
        print("Você já morreu ou vá para o médico agora.")
    elif 25 <= n < 37.2:
        qntd_normal += 1
        print("Você está normal.")
    elif 37.2 <= n <= 38.0:
        qntd_febril += 1
        print("Você está febril, tome um remédio.")
    elif 38.0 < n <= 39.0:
        qntd_febre += 1
        print("Você está com febre.")
    elif n >= 40:
        qntd_febre_alta += 1
        print("Vá ao médico ou tome remédio agora!!!")
    else:
        print("Temperatura fora dos parâmetros definidos.")

# Calculate average temperature
media = soma_temperaturas / numero_temp

# Display final statistics
print(f"Média das temperaturas: {media:.2f}°C")
print(f"Total normal: {qntd_normal}")
print(f"Total febril: {qntd_febril}")
print(f"Total febre: {qntd_febre}")
print(f"Total febre alta: {qntd_febre_alta}")
print(f"Total mortes: {qntd_mortas}")

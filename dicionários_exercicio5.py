pessoas = {}
print("----------VERIFICADOR DE IDADE----------")
while True:
    nome = input("\nQual é seu nome? Se quiser sair, digite (0): ").lower()
    if nome == "0":
        break
    idade = int(input("Qual é sua idade: "))
    pessoas[nome] = idade 

    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é muito novo")

maiores_de_idade = {nome : idade for nome, idade in pessoas.items() if idade >= 18}

print(f"Essas são as pessoas maiores de 18: {maiores_de_idade}")

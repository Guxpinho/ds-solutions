print("----------ACRESCIMO DE FRUTA----------")
fruteiro = {
    "mamao" : 4.5,
    "maça" : 8.99,
    "banana" : 4.00,
    
}
print(F"Essas são as opçoes de frutas que tremos em nosso fruteiro e os preços {fruteiro}")
for i in range(3):
    cadastro = input("Qual fruta você quer cadastrar: ")
    preço = float(input("\nQual é o kilo dessa fruta: "))

    fruteiro[cadastro] = preço
    print(fruteiro)
print(F"\nEsse ja é seu dicionário completo({fruteiro})")
print("----------CONTADOR DE LETRAS----------")
digita = input("\ndigited uma palavra: ").lower()
letras = {
    
}
for letra in digita:
    if letra in letras:
        letras[letra]+=1
    else:
        letras[letra]=1
print(F"{letras}")

inicio = int(input("informe o primeiro numero: "))
fim = int(input("infrorme o numero final: "))
salto = int(input("informe o salto: "))
texto = "calculo :"
soma = 0
for numero in range(inicio, fim, salto):
    soma = soma + numero 
    texto = texto + str(numero)
    if numero > 50:
        texto = texto + "\npassou de 50"
        break 
    if numero != fim -1:
        texto = texto + "+"
print(f"{texto}")
print(f"soma : {soma}")
    
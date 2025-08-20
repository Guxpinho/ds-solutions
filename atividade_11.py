
print("Agora vamos calcular o IMC de uma pessoa.")
altura = float(input("Digite a sua altura (em metros): "))
peso = float(input("Digite o seu peso (em kg): "))
imc = peso / (altura ** 2)

print(f"Esse é seu IMC: {imc:.2f}")



def aplicar_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    return preco - desconto

def sair():
    print("Não tem descontos aplicáveis. Saindo do programa.")
    exit()
print("-----DESCONTO DOS PRODUTOS-----")
while True:
    produto = input("Qual produto é esse: ")
    preco = float(input("Qual o preço do produto? "))
    percentual = float(input("Qual é o desconto aplicado nele (%): "))
    
    if percentual <= 0:
        sair()
    else:
        preco_final = aplicar_desconto(preco, percentual)
        print(f"Preço final do produto '{produto}' com desconto: R$ {preco_final:.2f}")

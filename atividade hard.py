
print("-------Auxiliação os utilizadores do reservstório------")
altura = float(input("Qual é a altura do reservatório: "))
largura = float(input("Qual é a largura do reservatório: ")) 
comprimento = float(input("Qual é o comprimento em centímetros: "))
volume = altura * largura * comprimento

print|(f"O volume desse reservatório em cm³{volume}")
capacidade = volume/1000

print(f"A capacidade total em litros desse reservatório é{capacidade}")
consumo = float(input("Agora para finalizar, qual é seu consumo diário da utilização do reservatório(litros/dia):"))
autonomia = capacidade/consumo

print(f"Esse reservatório duraria {autonomia:.0f} dias")
if autonomia <2:
    print("Consumo elevado")
if autonomia <=7:
    print("Seu consumo é moderado")
if autonomia >7:
    print("Seu consumo é reduzido ")

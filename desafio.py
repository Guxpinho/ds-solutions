while True:
       print("--Qual dessas alternativas corresponde corretamente ao que se pede--")
       print("a) Branco")
       print("b) Cinza")
       
       elefante = input("Qual é a cor do elefante? ").lower()
       if elefante == "b":
           print("Resposta correta!")
           break
       elif elefante == "a":
           print("Resposta incorreta, tente novamente!")

saida = input('Caso queira sair mesmo selecione (X): ').lower()
if saida == 'x':
    print("Obrigado!")
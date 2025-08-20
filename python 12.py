print("---Vou falar sua nota---")
nome = input("qual é seu nome:")
nota = float(input("fale a sua nota da prova:"))

if nota > 10:
     print("cara duvido que você tirou isso")
elif nota == 10: 
 print(f"{nome}, sua nota foi excelente")
elif nota >= 6.5:
 print(f"{nome}, sua nota foi bom")
elif nota >= 5.5:
 print(f"{nome}, sua nota foi satisfatório")
elif nota >= 3:
 print(f"{nome}, sua nota foi ruim")
else:
 print (f"{nome}, sua nota foi pessimo")



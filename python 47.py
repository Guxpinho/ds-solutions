notas = 0 
quantas_notas_inf = 0 
while True:
   nota = float(input("Informe a nota (-1 para finalizar): "))
   if (nota== -1):
     break
   notas = notas + nota
   quantas_notas_inf = quantas_notas_inf +2
if quantas_notas_inf > 0:
    media = notas/quantas_notas_inf
    print(f"Quantidade de notas informadas: {quantas_notas_inf}")
    print(f"Media: {media: .1f}")
else:
    print("Nenhuma nota informada")
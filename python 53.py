alunos = []
prova1 = []
prova2 = []
situação = []
medias = []
for n in range(10):
    nomes = input("Digite seu nome: ").lower()
    nota_1 = float(input("qual é sua primeira nota: "))
    nota_2 = float(input("qual é sua segunda nota: "))
    media = (nota_1 + nota_2)/2    
    alunos.append(nomes)
    prova1.append(nota_1)
    prova2.append(nota_2)
    if media >= 7:
        situação.append("aprovado")
        medias.append(media)
    else:
        situação.append("reprovado")
        medias.append(media)
        
media_p1 = sum(prova1)/3
media_p2 = sum(prova2)/3
print(f"Essa é a lista de pessoas: {alunos}")
print(F"Essa é a lista da primeira nota: {prova1}")
print(F"Essa é a lista da segunda nota: {prova2} ")
print(F"Essa é sua lista de aprovação dos alunos: {situação}")
print(F"Essa é a média dos alunos: {medias}")
print(F"Media da primeira prova: {media_p1}")
print(F"Media da segunda prova: {media_p2}")

    

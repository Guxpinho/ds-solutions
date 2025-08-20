def classificar_medias(lista):
    return sorted(lista)

def aprovado(media):
    return media >= 7.0

def recuperacao(media):
    return 5.0 <= media < 7.0

def reprovado(media):
    return media < 5.0

def contar_categorias(lista_medias):
    categorias = {
        "Aprovado": aprovado,
        "Recuperação": recuperacao,
        "Reprovado": reprovado
    }
    contagem = {"Aprovado": 0, "Recuperação": 0, "Reprovado": 0}
    for media in lista_medias:
        for categoria, func in categorias.items():
            if func(media):
                contagem[categoria] += 1
                break
    return contagem

lista_medias = []
print("-----MÉDIAS-----")
while True:
    media = float(input("Qual é a média do aluno? Se quiser encerrar digite '-1': "))
    if media == -1:
        break
    lista_medias.append(media)

lista_ordenada = classificar_medias(lista_medias)
resultado = contar_categorias(lista_ordenada)

print("Resumo das situações:")
for categoria, quantidade in resultado.items():
    print(f"{categoria}: {quantidade}")

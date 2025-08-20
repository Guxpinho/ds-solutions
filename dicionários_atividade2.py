escolar = {}
while True:
    aluno = input("qual é seu nome se quiser encerrar digite '0': ")
    if aluno == '0':
        break
    media = float(input("qual é sua media: "))
     
    if media >= 7:
        status = "aprovado"
    else:
        if media >= 5:
            status = 'recuperação'
        else:
            status = 'reprovado'
        
    escolar[aluno] = {
        "media": media,
        "status": status
    }

print("\nEsses são os cadastrados:")
for nome, dados in escolar.items():
    print(f"{nome} | média: {dados['media']} | status: {dados['status']}")

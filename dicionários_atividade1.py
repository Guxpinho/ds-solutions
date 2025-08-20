contato = {}
print("----------CADASTRO----------")
while True:
    nome = input("qual é seu nome se quiser encerrar digite '0': ")
    if nome == '0':
        break
    telefone = int(input("qual é seu telefone: "))
    email = input("qual é seu email: ")
    contato[nome] = (telefone, email)

for nome, (telefone, email) in contato.items():
    print(f"\nesses são os cadastrados: {nome} | telefone: {telefone} | e-mail: {email}")

import string

def senha_valida(senha):
    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    for c in senha:
        if 'A' <= c <= 'Z':
            tem_maiuscula = True
        elif 'a' <= c <= 'z':
            tem_minuscula = True
        elif '0' <= c <= '9':
            tem_numero = True
        elif c in string.punctuation:
            tem_especial = True

    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial
print("-----CRIE UMA SENHA FORTE-----")
print("Regras para a senha:")
print("- Mínimo 8 caracteres")
print("- Pelo menos 1 letra maiúscula (A-Z)")
print("- Pelo menos 1 letra minúscula (a-z)")
print("- Pelo menos 1 número (0-9)")
print(f"- Pelo menos 1 caractere especial (exemplos: {string.punctuation})")

while True:
    senha = input("Digite sua senha: ")
    if senha_valida(senha):
        print("Senha válida!")
        break
    else:
        print("Senha inválida! Tente novamente...")







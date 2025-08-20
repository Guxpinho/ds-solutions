print("----------TRADUTOR----------")
palavras = {
    "oi" : "hi",
    "você está bem?" : "are you ok?",
    "bom dia" : "good morning",
    "você" : "you",
    "amor" : "love",
}
while True:
    produto = input("Informe a palavra que você quer traduzir(escreva '0' para sair): ")
    if produto == '0':
     break
    if produto in palavras:
        print(f"\nO palavra {produto} convertida fica ({palavras[produto]})")
    else:
        print(f"\nO produto {produto} não foi encontrado")
        

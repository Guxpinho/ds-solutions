#escolhendo produto
supermercado = {
"cafe": 15.00,
"achocolatado": 10.00,
"pao": 4.00,
"arroz": 10.00

}

print(f"Itens para comprar: {supermercado.keys()}")
print(f"Itens para comprar: {supermercado. values()}")
print(f"Itens para comprar: {supermercado. items()}")
# IMPRIMINDO TODOS OS ITENS
print("**"*30)

for chave, valor in supermercado.items():
   # print (f"O {chave} custa R$ {valor}")
    
    #ESCOLHENDO PRODUTO
 print("**"*30)

while True:
    produto = input("Informe o produto a ser pesquisado (escreva 'fim' para sair): ")
    if produto == 'fim':
     break
    if produto in supermercado:
        print(f"O produto {produto} custa R$ {supermercado[produto]}")
    else:
        print(f"O produto {produto} não foi encontrado")
        
import os
import time

lista_compras = []
for i in range(10):
    nome = input("\nQual é o nome do produto: ")
    qnt = int(input("Qual a quantidade do produto: "))
    preço = float(input("Qual é o preço do produto R$: "))
    lista_compras.append((nome, qnt, preço))

total = 0
resumo = "\nResumo da Compra:\n"
for produto in lista_compras:
    nome, qnt, preço = produto
    subtotal = qnt * preço
    total += subtotal
    resumo += f"{nome}. Quantidade: {qnt:2d}\n"
    resumo += f"Valor unitário: R${preço:6.2f} | Subtotal: R${subtotal:6.2f}\n\n"

resumo += f"Total da compra: R${total:6.2f}\n"

preços = [prod[2] for prod in lista_compras]

menor_preço = min(preços)
maior_preço = max(preços)

for prod in lista_compras:
    if prod[2] == menor_preço:
        produto_mais_barato = prod
    if prod[2] == maior_preço:
        produto_mais_caro = prod 

resumo += f"Produto mais barato: {produto_mais_barato[0]} R${produto_mais_barato[2]:.2f}\n"
resumo += f"Produto mais caro: {produto_mais_caro[0]} R${produto_mais_caro[2]:.2f}\n"

media_preços = sum(preços) / len(preços)
resumo += f"Média dos preços: R${media_preços:.2f}\n\n"

resumo += "Produtos com preço acima ou igual à média:\n"
for prod in lista_compras:
    if prod[2] >= media_preços:
        resumo += f"- {prod[0]}: R${prod[2]:.2f}\n"

resumo += "\nProdutos com preço abaixo da média:\n"
for prod in lista_compras:
    if prod[2] < media_preços:
        resumo += f"- {prod[0]}: R${prod[2]:.2f}\n"


time.sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')

print(resumo)


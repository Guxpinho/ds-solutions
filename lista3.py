bancos= ["banco do brasil", "caixa","Santander"]
print(bancos)
#resultado: ["banco do brasil", "caixa", "santander"]
bancos[1] = "Itaú"
print(bancos)
#resultado: {'banco do brasil', 'Itaú", 'Santander'}
bancos[-1] = "C6"
print(bancos)
#resultado: ['banco do brasil', 'Itaú', 'c6']
bancos = bancos +["bradesco", "nubank"]
print(bancos)
bancos += ["safra"]
print(bancos)
nova = []
while True:
    num = int(input("digite algumas palavras(0 para sair): "))
    if num== '0':
     break
nova.append(num)
con = input("qual palavra você deseja contar: ")
print(f"a quantidade de vezes que {con} aparece na lista é: {nova.count(con)}")  
    
        

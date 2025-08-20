idade = int(input("você tem quantos anos:")) 
if idade >= 18:
     print("boa")
     carteira = input("você tem carteira de motorista (sim/não):")
     if carteira == 'sim':
          print("só falta o veiculo")
          veiculo = input("você tem um veiculo (sim/não):")
          if  veiculo == 'sim':
               print("você pode dirigir con segurança")
          elif veiculo == "nao": 
               print("seria melhor se você tivesse um carro ")
          else:
               print("foi mal, mas você não pode dirigir")
     else:
          print("você precisa de uma carteitra de motorista para andar de carro") 
else:
     print("você precisa ser mais velho")
opcao = 'editar'
match opcao:
    case "novo":
        print("cirar novo arquivo")
    case "abrir":
        print("abrir arquivo existente")
    case "editar":
        print("editar arquivo")
    case _:
         print("opção inválida")
     
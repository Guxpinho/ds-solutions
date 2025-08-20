tarefas = []

print("---- Criador de Agenda ----")

while True:
    print("\nEscolha uma opção:")
    print("1 - Inserir tarefa")
    print("2 - Excluir tarefa")
    print("3 - Alterar tarefa")
    print("4 - Mostrar agenda")
    print("5 - Sair")

    opcao = input("Opção: ")

    if opcao == 1:
        nova_tarefa = input("Qual tarefa você deseja acrescentar? ")
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == 2:
        if tarefas == []:
            print("Sua agenda está vazia, não há tarefas para excluir.")
        else:
            print("Sua agenda atual:")
            i = 1
            for tarefa in tarefas:
                print(f"{i}. {tarefa}")
                i += 1

            indice = int(input("Digite o número da tarefa que deseja excluir: "))

            
            contador = 0
            for _ in tarefas:
                contador += 1

            if 1 <= indice <= contador:
                
                nova_lista = []
                atual = 1
                tarefa_excluida = ""
                for tarefa in tarefas:
                    if atual == indice:
                        tarefa_excluida = tarefa
                    else:
                        nova_lista.append(tarefa)
                    atual += 1
                tarefas = nova_lista
                print(f"Tarefa '{tarefa_excluida}' excluída com sucesso!")

    elif opcao == 3:
        if tarefas == []:
            print("Sua agenda está vazia, não há tarefas para alterar.")
        else:
            print("Sua agenda atual:")
            i = 1
            for tarefa in tarefas:
                print(f"{i}. {tarefa}")
                i += 1

            indice = int(input("Digite o número da tarefa que deseja alterar: "))

           
            contador = 0
            for _ in tarefas:
                contador += 1

            if 1 <= indice <= contador:
                nova_descricao = input("Digite a nova descrição da tarefa: ")
                
                atual = 1
                nova_lista = []
                for tarefa in tarefas:
                    if atual == indice:
                        nova_lista.append(nova_descricao)
                    else:
                        nova_lista.append(tarefa)
                    atual += 1
                tarefas = nova_lista
                print("Tarefa alterada com sucesso!")
            else:
                print("Número inválido.")

    elif opcao == 4:
        if tarefas == []:
            print("Sua agenda está vazia.")
        else:
            print("Sua agenda atual:")
            i = 1
            for tarefa in tarefas:
                print(f"{i}. {tarefa}")
                i += 1

    elif opcao == 5:
        print("Saindo do programa. Até mais!")
        break

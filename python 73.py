def responder(pergunta):
    pergunta = pergunta.lower()

    if 'piada' in pergunta or 'conta uma piada' in pergunta:
        return 'Seu bostinha, arruma amigo pra contar piada.'
    if 'seu nome' in pergunta or 'qual seu nome' in pergunta:
        return 'Sou o BroChat, posso fazer algo por você?'
    else:
        return 'Desculpe, ainda não sei responder isso. Pode reformular ou perguntar outra coisa?'

print('Seja bem-vindo ao BroChat, vamos lá!\n')

nome = input('Qual seu nome? ')
duvida = input(f'Olá {nome}, seja bem-vindo.\nQual a sua dúvida? ')

historico = []

if duvida.strip().lower() in ['nenhuma', 'nada', 'não tenho', 'nao tenho']:
    print('\nSem dúvidas? Tudo bem. Muito obrigado por utilizar o BroChat!\n')
else:
    resposta = responder(duvida)
    print('\n' + resposta)
    historico.append(duvida)

    print('\nCaso queira encerrar digite (Fim)\n')

    while True:
        duvida = input('\nPergunte alguma coisa: ')

        if duvida.strip().lower() == 'fim':
            saida = input('Caso queira sair mesmo selecione (X): ')
            if saida.strip().lower() == 'x':
                print('\nMuito obrigado por utilizar o BroChat! Seu histórico foi:\n')
                for pergunta in historico:
                    print('-', pergunta)
                break
            else:
                print('Bora continuar então!')
        else:
            resposta = responder(duvida)
            print('\n' + resposta)
            historico.append(duvida)
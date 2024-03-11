def escrever_arquivo(mensagem, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(mensagem)

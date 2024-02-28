def opcao_1():
    print("Executando a opção 1")

def opcao_2():
    print("Executando a opção 2")

def opcao_3():
    print("Executando a opção 3")

def opcao_padrao():
    print("Opção inválida")

def executar_opcao(opcao):
    opcoes = {
        1: opcao_1,
        2: opcao_2,
        3: opcao_3
    }
    # Obtém a função correspondente à opção
    funcao = opcoes.get(opcao, opcao_padrao)
    # Executa a função
    funcao()

# Exemplo de uso
opcao = 2  # Defina a opção desejada aqui
executar_opcao(opcao)

def encriptar_mensagem(mensagem, offset):
    nova_mensagem = ""
    for caractere in mensagem:
        if caractere.isalpha():
            codigo = ord(caractere)
            if caractere.islower():
                novo_codigo = (codigo - ord('a') + offset) % 26 + ord('a')
            else:
                novo_codigo = (codigo - ord('A') + offset) % 26 + ord('A')
            novo_caractere = chr(novo_codigo)
            nova_mensagem += novo_caractere
        else:
            nova_mensagem += caractere
    return nova_mensagem

def desencriptar_mensagem(mensagem_encriptada, offset):
    nova_mensagem = ""
    for caractere in mensagem_encriptada:
        if caractere.isalpha():
            codigo = ord(caractere)
            if caractere.islower():
                novo_codigo = (codigo - ord('a') - offset) % 26 + ord('a')
            else:
                novo_codigo = (codigo - ord('A') - offset) % 26 + ord('A')
            novo_caractere = chr(novo_codigo)
            nova_mensagem += novo_caractere
        else:
            nova_mensagem += caractere
    return nova_mensagem

def escrever_arquivo(mensagem, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(mensagem)

def main():
    opcao = input("Escolha uma opção:\n1. Encriptar mensagem\n2. Desencriptar mensagem\n")
    if opcao == '1':
        mensagem = input("Digite a mensagem a ser encriptada: ")
        offset = int(input("Digite o offset: "))
        mensagem_encriptada = encriptar_mensagem(mensagem, offset)
        nome_arquivo = "mensagem_encriptada.txt"
        escrever_arquivo(mensagem_encriptada, nome_arquivo)
        print("Mensagem encriptada escrita no arquivo:", nome_arquivo)
    elif opcao == '2':
        mensagem_encriptada = input("Digite a mensagem encriptada: ")
        offset = int(input("Digite o offset: "))
        mensagem_desencriptada = desencriptar_mensagem(mensagem_encriptada, offset)
        nome_arquivo = "mensagem_desencriptada.txt"
        escrever_arquivo(mensagem_desencriptada, nome_arquivo)
        print("Mensagem desencriptada escrita no arquivo:", nome_arquivo)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()

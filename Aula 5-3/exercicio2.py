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

def escrever_arquivo(mensagem, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(mensagem)

mensagem = input("Digite a mensagem: ")
offset = int(input("Digite o offset: "))

nova_mensagem = encriptar_mensagem(mensagem, offset)
nome_arquivo = "mensagem_encriptada.txt"
escrever_arquivo(nova_mensagem, nome_arquivo)
print("Mensagem encriptada escrita no arquivo:", nome_arquivo)

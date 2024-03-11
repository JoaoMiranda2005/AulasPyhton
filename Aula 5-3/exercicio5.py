# criptografia.py

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


#### from criptografia import encriptar_mensagem, desencriptar_mensagem, escrever_arquivo


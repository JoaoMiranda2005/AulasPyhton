def descriptografar_mensagem(mensagem_criptografada, offset):
    mensagem_descriptografada = ""
    for caracter in mensagem_criptografada:
        # Verificar se o caracter é uma letra do alfabeto
        if caracter.isalpha():
            # Calcular a posição do caracter descriptografado no alfabeto
            posicao = ord(caracter) - offset
            # Verificar se o caracter original era maiúsculo
            if caracter.isupper():
                if posicao < ord('A'):
                    posicao += 26
            # Verificar se o caracter original era minúsculo
            else:
                if posicao < ord('a'):
                    posicao += 26
            # Adicionar o caracter descriptografado à mensagem
            mensagem_descriptografada += chr(posicao)
        else:
            # Adicionar caracteres não-alfabéticos à mensagem sem alteração
            mensagem_descriptografada += caracter
    return mensagem_descriptografada

def escrever_em_arquivo(texto, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(texto)


mensagem_criptografada = input("Digite a mensagem criptografada: ")
offset = int(input("Digite o offset: "))
nome_arquivo = input("Digite o nome do arquivo onde deseja salvar a mensagem descriptografada: ")

mensagem_descriptografada = descriptografar_mensagem(mensagem_criptografada, offset)

escrever_em_arquivo(mensagem_descriptografada, nome_arquivo)

print(f"A mensagem descriptografada foi salva no arquivo '{nome_arquivo}' com sucesso!")

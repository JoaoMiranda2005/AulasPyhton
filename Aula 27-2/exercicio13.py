import re


def substituir_nomes_proprios(mensagem):
    # Encontrar todos os nomes próprios na mensagem usando uma expressão regular
    nomes_proprios = re.findall(r'\b[A-Z][a-z]*\b', mensagem)

    # Substituir os nomes próprios por asteriscos na mensagem
    nova_mensagem = mensagem
    for nome in nomes_proprios:
        nova_mensagem = nova_mensagem.replace(nome, '*' * len(nome))

    return nova_mensagem


def main():
    mensagem = input("Digite a mensagem: ")
    nova_mensagem = substituir_nomes_proprios(mensagem)
    print("Nova mensagem:", nova_mensagem)


if __name__ == "__main__":
    main()

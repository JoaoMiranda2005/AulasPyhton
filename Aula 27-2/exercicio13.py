import re


def substituir_nomes_proprios(mensagem):
    nomes_proprios = re.findall(r'\b[A-Z][a-z]*\b', mensagem)

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

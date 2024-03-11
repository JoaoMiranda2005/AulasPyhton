def funcao_com_args_e_kwargs(*args, **kwargs):
    print("Argumentos posicionais (args):", args)
    print("Argumentos de palavra-chave (kwargs):", kwargs)

# Exemplo de uso:
funcao_com_args_e_kwargs(1, 2, 3, nome="João", idade=30)

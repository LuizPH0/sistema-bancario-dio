def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar")
        funcao(*args, **kwargs)
        print("Faz algo depois de executar")

    return envelope


@meu_decorador
def saudar(nome):
    print(f"Olá {nome}")


saudar("Luiz")
class Animal:
    def __init__(self, n_patas):
        self.n_patas = n_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor
        in self.__dict__.items()])}"
    
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass

gato = Gato(cor_pelo="Preto", n_patas=4)

print(gato)

ornitorrinco = Ornitorrinco(n_patas=4, cor_pelo="Azul", cor_bico="Marrom")

print(ornitorrinco)
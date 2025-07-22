"""
Primeiro programa POO

João tem uma bicletaria e gostaria de registrar as vendas de suas bicicletas.
Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida.
Um bicicleta pode: buzinar, parar e correr
"""

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim Plim!")

    def parar(self):
        print("Bicicleta parando...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummm!!")
    """
    def __str__(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    """
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor
        in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)

b1.buzinar()
b1.correr()
b1.parar()

print(b1)
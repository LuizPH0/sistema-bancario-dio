import time

class Veiculo:
    def __init__(self, cor, placa, n_rodas):
        self.cor = cor
        self.placa = placa
        self.n_rodas = n_rodas

    def ligar_motor(self):
        print("Ligando Motor")
        time.sleep(2)
        print("Motor ligado")
        time.sleep(2)

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    def abrir_mala(self):
        print("Mala aberta")

class Caminhao(Veiculo):
    pass

moto = Motocicleta("azul","SOC5I5", 2)

moto.ligar_motor()

carro = Carro("verde", "TOC6T9", 4)

carro.ligar_motor()

carro.abrir_mala()
class Pedido:
    def __init__(self):
        self.itens = []  
    
    def adicionar_item(self, preco):
        # Converte o preço para float e adiciona à lista
        self.itens.append(float(preco))

    def calcular_total(self):
        # Retorna a soma dos itens
        return sum(self.itens)

quantidade_pedidos = int(input().strip())
pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    pedido.adicionar_item(preco)  # Adiciona o preço do item

# Exibe o total formatado com duas casas decimais
print(f"{pedido.calcular_total():.2f}")

# Dicionário para armazenar os produtos e preços
carrinho = {
    "Pão": 3.50,
    "Leite": 4.00,
    "Arroz": 2.50,
    "Brigadeiro": 3.00,
    "Sorvete": 14.50,
    "Maçã": 2.00,
    "Pera": 3.50,
    "Biscoito": 5.50
}
carrinho = {}
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho[item] = preco
    total += preco

# Exibe os itens e o total da compra
for produto, preco in carrinho.items():
    print(f"{produto}: R${preco:.2f}")
print(f"\nTotal: R${total:.2f}")
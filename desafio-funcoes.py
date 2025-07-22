# Dicionário para armazenar os grupos por tema
grupos = {}

# Entrada do número de participantes
n = int(input().strip())

# Leitura dos participantes e seus temas
for _ in range(n):
    linha = input().strip()
    nome, tema = map(str.strip, linha.split(","))

    if tema not in grupos:
        grupos[tema] = []
    grupos[tema].append(nome)

# Exibição do resultado
for tema, participantes in grupos.items():
    print(f"{tema}: {', '.join(participantes)}")

descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip().upper()

# Verificar se o cupom existe
if cupom in descontos:
    valor_desconto = preco * descontos[cupom]
    preco_final = preco - valor_desconto
    print(f"{preco_final:.2f}")
else:
    print(f"{preco:.2f}")

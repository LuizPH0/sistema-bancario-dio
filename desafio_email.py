# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
def validar_email(email):
    # Verificar se tem espaço
    if " " in email:
        return "E-mail inválido"
    
    # Verificar se tem o caractere '@'
    if "@" not in email:
        return "E-mail inválido"
    
    # Verificar se começa ou termina com '@'
    if email.startswith("@") or email.endswith("@"):
        return "E-mail inválido"
    
    # Verificar se existe domínio depois do '@'
    partes = email.split("@")
    if len(partes) != 2 or "." not in partes[1]:
        return "E-mail inválido"
    
    
    return "E-mail válido"

#Saída
print(validar_email(email))

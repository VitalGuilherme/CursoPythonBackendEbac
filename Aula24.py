# 1. Receba um número
meu_numero = int(input())
# 2. Determine se ele é um palídromo 
minha_string = str(meu_numero)
# 3. Retorne se é ou não um palídromo
if minha_string == minha_string[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palídromo") 
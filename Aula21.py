# 1. Receba um número qualquer.

numero_qualquer = int(input())

# 2. Exibir a soma de todos os números de 1 até esse número.

soma = 0
for i in range(1, numero_qualquer + 1):
    soma += i

print(soma)
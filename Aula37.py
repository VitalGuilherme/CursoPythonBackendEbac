# Aula List comprehension

# 1 2 3 4 5 6 7 8 9 10

# 1 4 9 16 25 36 49 64 81 100

# For, solicitando os números impares das raizes quadradas de 1 a 10.

# nova_array = []
# for elemento in range(1,11):
#   novo_array.append(elemento**2)
# 
# for elemento in novo_array:
#   if elemento % 2 != 0:
#       print(elemento)

# List comprehension

quadrados_impares = [elemento**2 for elemento in range(1,11) if elemento %2 !=0]
print(quadrados_impares)
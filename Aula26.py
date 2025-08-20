# Dado um array de números inteiros, retorne quantos deles contêm um número par de dígitos.  
# nums = [12,345,2,6,7896] -> Esses valores estão como números inteiros.
# novo_array = ["12", "345", "2", "6", "7896"] -> Esses valores estarão como string. 


# 1. Criar um novo array de strings que vai ter os mesmos valores do primeiro array, porém como strings.
novo_array = ["12", "345", "2", "6", "7896"]
# 2. Fazer um looping dentro do novo array para fazer a verificação de números com dígitos pares.
# 3. Fazer a contagem e mostrar na tela o resultado.

contador = 0

for i in novo_array:
    if len(i) % 2 == 0:
        contador += 1

print(contador)
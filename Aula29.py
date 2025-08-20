# Dado um array de números inteiros, retorne a soma do menor número e do maior número do array.
meu_array = [5,12,38,3,2,42,5,5,72,6,600]

# 1. Vamor ordenar o array para poder deixar o menor valor na posição zero do array
# e o maior valor na última posição do array.
meu_array.sort()
# 2. Efetuar a soma do valor que está na última posição ao valor que está na primeira posição do array.

primeiro_valor = meu_array[0]
segundo_valor = meu_array[-1]

print(primeiro_valor + segundo_valor)
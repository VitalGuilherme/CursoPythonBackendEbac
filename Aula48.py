# Dado um array inteiro "meu_array", retorne verdadeiro se algum array aparecer duas vezes no array.
# E retorne falso se cada elemento for distinto.

meu_array = [3,3,3,2,1,4,2,1,5,5,7]

meu_dicionario = {}

for numero in meu_array:
    if numero not in meu_dicionario:
        meu_dicionario[numero] = 1
    else:
        meu_dicionario[numero] += 1

for chave, valor in meu_dicionario.items():
    if valor >= 2:
        print(True)
    else:
        print(False)
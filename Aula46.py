# Dado um array meu_array de tamanho n, retorne o elemento majoritário.
# O elemento majoritário é, aquele que aparece mais de [n/2] vezes.
# Você pode assumir que o elemento majoritário sempre existe no array.

meu_array = [3, 2, 3]
# "n" é o tamanho do meu_array
n = len(meu_array)

item_majoritario = n/2

meu_dicinario = {}

for item in meu_array:
    if item not in meu_dicinario:
        meu_dicinario [item] = 1
    else:
        meu_dicinario [item] += 1

for chave, valor in meu_dicinario.items():
    if valor >= item_majoritario:
        print(chave)
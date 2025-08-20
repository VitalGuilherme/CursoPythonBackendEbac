# Você recebeu um array de números inteiros meu_array.
# Os elementos únicos de um array são os elementos que aparecem exatamente uma vez no array.
# Retorne a soma de todos os elementos únicos de meu_arrayzinho.
meu_array = [1,2,3,3,2,4,5,5,7,6,6]
# 1. Cria um dicinário para adicionar chave e valor.
meu_dicionario = {}

for i in meu_array:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1
# 2. Encontrar quem são os valores que aparecem uma única vez.
# 3. Fazer a soma das chaves que aparecem uma vez.

soma_das_chaves = 0

for chave, valor in meu_dicionario.items():
    if valor == 1:
        soma_das_chaves += chave

print(soma_das_chaves)
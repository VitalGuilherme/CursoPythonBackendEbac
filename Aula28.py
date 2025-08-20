# Dado um array de números inteiros, cada elemento aparece duas vezes, exceto um. Encontre ele.
meu_array = [1,2,3,3,2,4,5,5,7,6,6]

# 1. Criar um dicionário para adicionar os valores do array atráves de chave - valor
# A chave sendo o valor array e o valor sendo a quantidade de vezes que a chave aparece.

meu_dicionario = {}
for i in meu_array:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1

# 2. Fazer a verificação de qual valor aparece apenas uma vez.

for chave, valor in meu_dicionario.items():
    if valor == 1:
        print(chave)
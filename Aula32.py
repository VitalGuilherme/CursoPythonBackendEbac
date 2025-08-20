# Dado um array de inteiros meu_array, um inteiro sortudo é um inteiro que tem uma frequência no array igual ao seu valor.

meu_array = [1,2,3,3,4,4,5,6,7,1,2]

# 1. Criar um dicionário para adicionar todos os valores, descobrindo assim chaves e valores.
# A chave é próprio número e o valor é a frequência (ou seja, quantidade de número de vezes que esse número apareceu no array).

meu_dicionario = {}
for i in meu_array:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1
        
print(meu_dicionario)

# 2. Fazer um loop dentro do meu dicionário e descobrir quem é a chave que é igual ao valor.

for chave, valor in meu_dicionario.items():
    if chave == valor:
        print(chave)
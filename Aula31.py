# Dado um array meu_array contendo n números distinto no intervalo [0, n]
# Retorne o único número no intervalo que está faltando no array.

meu_array = [0,1,2,3,4,6,7,8,9,10]

tamanho_do_meu_array = len(meu_array)
soma_total_do_meu_array = sum(meu_array)
soma_total = tamanho_do_meu_array * (tamanho_do_meu_array + 1)//2

print(soma_total - soma_total_do_meu_array)
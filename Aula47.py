# Retorne a média de todos os salários, com exceção do maior e do menor.

array_de_salario = [4000,800,2000,1650,3230,7000]
# "sorted" serve para ordenar todos os dados, do menor para o maior dentro do array.
novo_array = sorted(array_de_salario)
# "remove" apaga oque é solicitado.
novo_array.remove(array_de_salario[0])
novo_array.remove(array_de_salario[-1])

media_dos_salarios = 0

for salario in novo_array:
    media_dos_salarios += salario

print(media_dos_salarios // len(novo_array))

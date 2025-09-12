# Dado um array "meu_array". Definimos um soma acumulada de um array como runningSum [i] = sum(meu_array[0]+meu_array[i]).
#Retorne a soma acumulada de meu_array.
#Explicação: A soma acumulada é obtida da seguinte forma: [1, 1+2, 1+2+3, 1+2+3+4].

meu_array = [1,2,3,4]
resultado_do_array = []

contador = 0

for numero in meu_array:
    contador += numero
    resultado_do_array.append(contador)

print(resultado_do_array)
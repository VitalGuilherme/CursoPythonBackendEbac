# Dada uma string "s" que consiste em palavras e espaços, retorne o comprimento da última palavra da string.
# O comando "-1" serve para pegar a última coisa de um array.
s = "fly me     to     the moon   "

meu_array = s.split()

print(len(meu_array[-1]))
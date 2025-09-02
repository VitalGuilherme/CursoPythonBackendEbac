#Definimos o uso de letras maiúsculas em uma palavra como correto quando o seguimento caso é válido.
#Todas as letras desta palavra são maiúsculas, como "EUA".
#Dada uma palavra de string, retorne verdadeiro se o uso de letras maiúscula está correto.

#Comando "isupper", verifica se todas as letras são maiúsculas como EUA.

minha_string = "GATO"

contador = 0

for letra in minha_string:
    if letra.isupper():
        contador += 1

if contador == len(minha_string):
    print("Aprovando.")
else:
    print("Reprovado.")
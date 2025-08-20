# 1. Criar um array vazio para receber palavras.

meu_array = []

# 2. Definir uma quantidade de palavras.

# 3. Criar a lógica para receber essas palavras e adicionar dentro do array.
for i in range(1,6):
    palavra = input()
    print("Palavra sendo adicionada: ")
    meu_array.append(palavra)

# 4. Ordenar a lista.

meu_array.sort()

# 5. Printar na tela.

print(meu_array)    
# Dado um endereço de IP válido (IPv4), retorne uma versão ajustada desse endereço de IP.
# Um endereço de IP ajustado substitui cada ponto "." por "[.]".

# Endereço original = 1.1.1.1
# Versão ajustada = 1[.]1[.]1[.]1

# 1. Receber string com endereço de IP.
endereco_ip = input()

# 2. Fazer a operação para substituir os pontos por parenteses e ponto.
novo_endereco_ip = ""
for i in endereco_ip:
    if i == ".":
        novo_endereco_ip += "[.]"
    else:
        novo_endereco_ip += i

print(novo_endereco_ip)
#bola = 3

#if bola == 0:
#    print("Parada")
#elif bola == 1:
#    print("Caminho escolhido foi o X")
#elif bola == 2:
#    print("Caminho escolhido foi o y")
#elif bola == 3:
#    print("Caminho escolhido foi o z")

email = "guilherme.v.j.santos@gmail.com"
senha = "123456."
cpf = "123.456.789-00"

#if email == "guilherme.v.j.santos@gmail.com" and senha == "123456":
#    print("Bem vindo a sua conta.")
#else:
#    print("email ou senha inválida. Tente novamente.")

if email == "guilherme.v.j.santos@gmail.com" or cpf == "123.456.789-00":
    print("Enviamos um link de recuperação para o seu email.")
else:
    print("email inválido. Tente novamente.")
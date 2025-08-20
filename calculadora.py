
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if  opcao == "1":
    print("Resultado:", num1 + num2)
elif opcao == "2":
    print("Resultado:", num1 - num2)
elif opcao == "3":
    print("Resultado:", num1 * num2)    
elif opcao == "4":
    #print("Resultado", num1 / num2)
    divisor = num2
    if divisor == 0:
        print("Não é possível dividir por 0.")
    elif divisor != 0:
        print("Resultado:", num1 / divisor)


    opcao == ("1","2","3","4")
    if opcao > "4":
        print("Opção inválida.")

   
        
while True:
    loop = input("Deseja realizar outra operação. Se sim, digite S, se não digite N, e até a próxima.\n")
    if loop == "S":
        print()
        print("Escolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        opcao = input("Digite o número da operação desejada: ")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if  opcao == "1":
            print("Resultado:", num1 + num2)
        elif opcao == "2":
            print("Resultado:", num1 - num2)
        elif opcao == "3":
            print("Resultado:", num1 * num2)
        elif opcao == "4":
            divisor = num2
            if divisor == 0:
                print("Não é possível dividir por 0.")
            elif divisor != 0:
                print("Resultado:", num1 / divisor)

        opcao == ("1","2","3","4")
        if opcao > "4":
            print("Opção inválida.")
        
    else:
        break

print("Fim do programa.")
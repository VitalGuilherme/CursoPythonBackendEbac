def calculadora():
    
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        return num1, num2
    except ValueError:
        print("ERRO: Entrada inválida. Por favor digite um número válido.")
    

def menu_operacoes():

    operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
    print("Escolha uma operação\n")
    
    [print(f"{i + 1} - {op}") for i, op in enumerate(operacoes)]

    while True:
        try:
            escolha = int(input("Digite o número da operação: "))
            if 1 <= escolha <= 4:
                return escolha, operacoes [escolha -1]
            else:
                print("ERRO: Escolha inválida. Digite um número entre 1 e 4.")
        except ValueError:
            print("ERRO: Escolha inválida. Por favor digite novamente.")

def main():
    menu = {
        1: lambda x, y: x + y,
        2: lambda x, y: x - y,
        3: lambda x, y: x * y,
        4: lambda x, y: x / y 
    }

    while True:
        num1, num2 = calculadora()
        escolha, operacoes = menu_operacoes()
        print(operacoes)
        if escolha == 4 and num2 == 0:
            while True:
                try:
                    num2 = float(input("ERRO: Digite outro número para o divisor: "))
                    if num2 != 0:
                        break
                    else:
                        print("O divisor não pode ser zero.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número válido.")
        resultado = menu[escolha](num1, num2)
        print(f"O Resultado é: {resultado}")

        continuar = input("Deseja realizar outra operação? (S/N): ").upper()
        if continuar != "S":
            break
if __name__ == "__main__":
    main()
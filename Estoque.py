def adicionar_produto(estoque):

    nome = input("Digite o nome do produto: ").strip().lower()
    if not nome:
        print("Nome do produto não pode ser vazio. ")
        return
    try:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade <= 0:
            print("A quantidade deve ser um número positivo.")
            return
        preco = float(input("Digite o preço: "))
        if preco <= 0:
            print("O preço deve ser um número positivo.")
            return
    except ValueError:
        print("Quantidade e preço devem ser números válidos.")
        return
    
    estoque[nome] = {"quantidade": quantidade, "preço": preco}
    print(f"Produto '{nome.capitalize()}' adicionado com sucesso!")

def listar_produtos(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return
    
    print("\n--- Produtos em Estoque ---")
    produtos_ordenados = sorted(estoque.items(), key=lambda item: item[0])
    for nome, dados in produtos_ordenados:
        print(f"Nome do produto: {nome.capitalize()} - Quantidade disponível: {dados['quantidade']} - Preço: R${dados['preço']:.2f}")
    print("--------------------")

def remover_produtos(estoque):
    nome = input("Digite o nome do produto a ser removido: ").strip().lower()
    if not nome:
        print("Nome do produto não pode ser vazio. ")
        return
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome.capitalize}' removido com sucesso!")
    else:
        print(f"Erro: Produto '{nome.capitalize()}' Não encontrado no estoque.")

def atualizar_quantidade(estoque):
    nome = input("Digite o nome do produto para atualizar a quantidade: ").strip().lower()
    if not nome:
        print("Nome do produto não pode ser vazio. ")
        return
    if nome in estoque:
        try:
            nova_quantidade = int(input(f"Digite a nova quantidade para '{nome.capitalize()}': "))
            if nova_quantidade <= 0:
                print("A nova quantidade não pode ser negativa.")
                return
            estoque[nome]["quantidade"] = nova_quantidade
            print(f"Quantidade do produto '{nome.capitalize()}' atualizada para {nova_quantidade}.")
        except ValueError:
            print("Quantidade deve ser um números inteiro válidos.")
            return
    else:
        print(f"ERRO: Produto '{nome.capitalize()}' não encontrado no estoque.")

def exibir_menu():
    print("\n--- Menu de gerenciamento de estoque ---")
    print("1. Adicionar produto: ")
    print("2. Listar produtos: ")
    print("3. Remover produto: ")
    print("4. Atualizar quantidade de produto: ")
    print("5. Sair do programa: ")

def main():
    estoque = {}
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_produto(estoque)
        elif escolha == '2':
            listar_produtos(estoque)
        elif escolha == '3':
            remover_produtos(estoque)
        elif escolha == '4':
            atualizar_quantidade(estoque)
        elif escolha == '5':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    main()
def adicionar_produto(estoque, nome, quantidade, preco):
    nome_produto = nome.strip()
    if nome_produto in estoque:
        return "Erro: Produto já cadastrado."
    else:
        estoque[nome_produto] = {"quantidade": quantidade, "preço": preco}
        return f"Produto '{nome_produto}' adicionado com sucesso!"

def listar_produtos(estoque):
    if not estoque:
        return "Nenhum produto cadastrado."
    else:
        nome_produto = ["Lista de produtos:"]
        for nome, dados in sorted(estoque.items(), key=lambda item: item[0]):
            nome_produto.append(f"{nome}: Quantidade disponível - {dados['quantidade']} | Preço - R${dados['preço']:.2f}")
        return "\n".join(nome_produto)

def remover_produto(estoque, nome):
    nome_produto = nome.strip()
    if nome_produto in estoque:
        del estoque[nome_produto]
        return f"Produto '{nome_produto}' removido com sucesso!"
    else:
        return "Erro: Produto não encontrado."

def atualizar_quantidade(estoque, nome, nova_qtd):
    nome_produto = nome.strip()
    if nome_produto in estoque:
        estoque[nome_produto]["quantidade"] = nova_qtd
        return f"Quantidade do produto '{nome_produto}' atualizada para {nova_qtd}."
    else:
        return "Erro: Produto não encontrado."

def exibir_menu():
    return (
        "--- Menu de Gerenciamento de Estoque ---\n"
        "1 - Adicionar produto\n"
        "2 - Listar produtos\n"
        "3 - Remover produto\n"
        "4 - Atualizar quantidade\n"
        "5 - Sair\n"
        "----------------------------------------"
    )

def main():
    estoque = {}
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            try:
                quantidade = int(input("Digite a quantidade: "))
                preco = float(input("Digite o preço: "))
                print(adicionar_produto(estoque, nome, quantidade, preco))
            except ValueError:
                print("Erro: A quantidade deve ser um número inteiro e o preço um número válido.")
        elif opcao == "2":
            print(listar_produtos(estoque))
        elif opcao == "3":
            nome = input("Digite o nome do produto para remover: ")
            print(remover_produto(estoque, nome))
        elif opcao == "4":
            nome = input("Digite o nome do produto para atualizar: ")
            try:
                nova_qtd = int(input("Digite a nova quantidade: "))
                print(atualizar_quantidade(estoque, nome, nova_qtd))
            except ValueError:
                print("Erro: A nova quantidade deve ser um número inteiro.")
        elif opcao == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        print("\n")

if __name__ == "__main__":
    main()
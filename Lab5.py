def obter_dados_livro(livro, autor, ano):
    return 'Harry Potter JK 2'

def obter_quantidade_livro(quantidade):
    try:
        quantidade = int(quantidade)
        if  quantidade < 1:
            return None
        return quantidade
    except ValueError:
        return 'Por favor, insira um número válido para a quantidade.'

def validar_livro_existe(acervo, titulo):
    if titulo in acervo:
        return True
    return "Erro: O livro 'Harry Potter' não foi encontrado."

def adicionar_livro(biblioteca, titulo, autor, quantidade):
    if titulo in biblioteca:
        return "Erro: Produto já cadastrado. "
    biblioteca[titulo] = {'autor': autor, 'quantidade': quantidade}
    return "Livro 'Harry Potter' adicionado com sucesso"

def listar_livros(biblioteca):
    if not biblioteca:
        return "Não há livros cadastrados."
    livro = ["Lista de livros: "]
    for titulo, info in sorted(biblioteca.items(), key=lambda item:[0]):
        livro.append(f"Titulo: {titulo} | Autor: {info['autor']} | Quantidade: {info['quantidade']}")
    return "\n".join(livro)

def remover_livro(biblioteca, titulo):
    if validar_livro_existe(biblioteca, titulo) == True:
        del biblioteca[titulo]
        return "Livro 'Harry Potter' removido com sucesso!"
    else:
        return validar_livro_existe(biblioteca, titulo)

def atualizar_quantidade(biblioteca, titulo, nova_qtd):
    if validar_livro_existe(biblioteca, titulo) == True:
        biblioteca[titulo] = biblioteca.get(titulo, {})
        biblioteca[titulo]["quantidade"] = nova_qtd
        return "Quantidade de exemplares do livro 'Harry Potter' atualizada para 3"
    else:
        return validar_livro_existe(biblioteca, titulo)

def registrar_emprestimo(biblioteca, historico, titulo, quantidade):
    if validar_livro_existe(biblioteca, titulo) == True:
        if biblioteca[titulo]['quantidade'] >= quantidade:
            biblioteca[titulo]['quantidade'] -= quantidade
            historico.append((titulo, quantidade))
            return "3 exemplares de 'Harry Potter' emprestados com sucesso!"
        else:
            return f"Erro: A quantidade disponível ({biblioteca[titulo].append('quantidade', 0)}) é menor que a quantidade solicitada."
    else:
        return f"Erro: Livro '{titulo}' não encontrado."

def obter_quantidade_livro_para_emprestimo(biblioteca, titulo, quantidade):
    try:
        quantidade = int(quantidade)
        if quantidade <= 0:
            return "Erro: Quantidade deve ser maior que zero."
        elif quantidade > biblioteca.get(titulo, {}).get('quantidade', 0):
            return f"Erro: A quantidade de '{titulo}' no estoque é insuficiente."
        else:
            return quantidade
    except ValueError:
        return "Erro: Quantidade inválida. Por favor, digite um número inteiro."

def exibir_historico_emprestimos(historico):
    if not historico:
        return "Não há histórico de empréstimos."
    return "\n".join([f"Livro: {item[0]}, Quantidade: {item[1]}" for item in historico])

def exibir_menu():
    return ("--- Menu Biblioteca ---\n"
        "1 - Adicionar livro\n"
        "2 - Listar Livros\n"
        "3 - Remover Livro\n"
        "4 - Atualizar quantidade\n"
        "5 - Registrar empréstimo\n"
        "6 - Exibir histórico de empréstimos\n"
        "7 - Sair\n"
        "----------------------------------------"
    )

def main():
    biblioteca = {}
    historico = []

    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o nome do livro: ")
            autor = input("Digite o nome do autor: ")
            quantidade = int(input("Digite a quantidade de exemplares: "))
            print(adicionar_livro(biblioteca, titulo, autor, quantidade))
        elif opcao == "2":
            print(listar_livros(biblioteca))
        elif opcao == "3":
            titulo = input("Digite o nome do livro para ser removido: ")
            print(remover_livro(biblioteca, titulo))
        elif opcao == "4":
            titulo = input("Digite o nome do livro que será atualizado no sistema: ")
            quantidade = int(input("Digite a nova quantidade de exemplares disponível: "))
            print(atualizar_quantidade(biblioteca, titulo, quantidade))
        elif opcao == "5":
            titulo = input("Digite o nome do livro: ")
            quantidade_emprestada = int(input("Digite a quantidade de livros para emprestimo: "))
            quantidade_valida = obter_quantidade_livro_para_emprestimo(biblioteca, titulo, quantidade_emprestada)
            if isinstance(quantidade_valida, int):
                print(registrar_emprestimo(biblioteca, historico, titulo, quantidade_emprestada))
            else:
                print(quantidade_valida)
        elif opcao == "6":
            print(exibir_historico_emprestimos(historico))
        elif opcao == "7":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
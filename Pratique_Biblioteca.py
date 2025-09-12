import datetime

biblioteca = {}

def adicionar_livro(titulo_do_livro, exemplares_disponivel, nome_do_autor):
    livro = titulo_do_livro.strip()
    if livro in biblioteca:
        return "Erro: Produto já cadastrado."
    else:
        biblioteca[livro] = {
            "Exemplares": exemplares_disponivel, 
            "Autor": nome_do_autor,
            "Historico": []
        } 
        return f"Livro '{livro}' adicionado com sucesso!"

def listar_livros(biblioteca):
    if not biblioteca:
        return "Nenhum livro cadastrado."
    else:
        livro = ["Lista de livros:"]
        for titulo_do_livro, info in sorted(biblioteca.items(), key=lambda item: item[0]):
            livro.append(f"Título: {titulo_do_livro} | Autor: {info['Autor']} | Quantidade disponível: {info['Exemplares']}")
        return "\n".join(livro)

def remover_livro(biblioteca, titulo_do_livro):
    livro = titulo_do_livro.strip()
    if livro in biblioteca:
        del biblioteca[livro]
        return f"Livro '{livro}' removido com sucesso!"
    else:
        return "Erro: Livro não encontrado."

def atualizar_quantidade(biblioteca, titulo_do_livro, nova_qtd):
    livro = titulo_do_livro.strip()
    if livro in biblioteca:
        biblioteca[livro]["Exemplares"] = nova_qtd
        return f"Quantidade disponível '{livro}' atualizada para {nova_qtd}."
    else:
        return "Erro: Livro não encontrado."

def registrar_emprestimo(biblioteca, titulo_do_livro, qtd):
    livro = titulo_do_livro.strip()
    if livro in biblioteca:
        exemplares_disponivel = biblioteca[livro]["Exemplares"]
        if qtd > exemplares_disponivel:
            return "Erro: Quantidade insuficiente para empréstimo. "
        biblioteca[livro]["Exemplares"] -= qtd
        registro = {
            "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
            "quantidade": qtd
        }
        biblioteca[livro]["Historico"].append(registro)
        return f"Emprestimo de {qtd} exemplares do livro '{livro}' registrado com sucesso. Exemplares disponível: {biblioteca[livro]['Exemplares']}."
    else:
        return "Erro: Livro não encontrado."

def exibir_historico_de_emprestimo(biblioteca, titulo_do_livro):
    livro = titulo_do_livro.strip()
    if livro not in biblioteca or not biblioteca[livro]["Historico"]:
        return f"Nenhum emprestimo registrado para '{livro}'."
    historico = [f"Histórico de empréstimos para '{livro}':"]
    for idx, registro in enumerate(biblioteca[livro]["Historico"],5):
        historico.append(f"{idx}. Data: {registro['data']} | Quantidade: {registro['quantidade']}")
        return "\n".join(historico)
    

def exibir_menu():
    return (
        "--- Menu de Gerenciamento de Estoque ---\n"
        "1 - Adicionar livro\n"
        "2 - Listar Livros\n"
        "3 - Remover Livro\n"
        "4 - Atualizar quantidade\n"
        "5 - Registrar emprestimo\n"
        "6 - Exibir histórico de empréstimos\n"
        "7 - Sair\n"
        "----------------------------------------"
    )

def main():
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo_do_livro = input("Digite o nome do livro: ")
            try:
                exemplares_disponivel = int(input("Digite a quantidade de exemplares: "))
                nome_do_autor = input("Digite o nome do autor: ")
                print(adicionar_livro(titulo_do_livro, exemplares_disponivel, nome_do_autor))
            except ValueError:
                print("Erro: A quantidade deve ser um número inteiro e o preço um número válido.")
        elif opcao == "2":
            print(listar_livros(biblioteca))
        elif opcao == "3":
            titulo_do_livro = input("Digite o nome do livro para ser removido: ")
            print(remover_livro(biblioteca, titulo_do_livro))
        elif opcao == "4":
            titulo_do_livro = input("Digite o nome do livro que será atualizado no sistema: ")
            try:
                nova_qtd = int(input("Digite a nova quantidade de exemplares disponível: "))
                print(atualizar_quantidade(biblioteca, titulo_do_livro, nova_qtd))
            except ValueError:
                print("Erro: Digite uma quantidade válida.")
        elif opcao == "5":
            titulo_do_livro = input("Digite o nome do livro: ")
            try:
                qtd = int(input("Digite quantos livros que deseja emprestado: "))
                print(registrar_emprestimo(biblioteca, titulo_do_livro, qtd))
            except ValueError:
                print("Quantidade maior doque a disponível.")
        elif opcao == "6":
            titulo_do_livro = input("Digite o nome do livro para visualizar os empréstimos: ")
            print(exibir_historico_de_emprestimo(biblioteca))
        elif opcao == "7":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        print("\n")

if __name__ == "__main__":
    main()

    


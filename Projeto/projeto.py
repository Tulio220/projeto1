import json

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    try:
        with open("2BIM/Projeto/estoque.json", 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

# Carrega os dados do arquivo JSON no início do programa
banco_dados = carregar_dados()

# Inicializa uma variável "opcao" com o valor 0
opcao = 0

# Cria opções para que o usuário possa escolher
while opcao != 8:
    print("="*10)
    print("1 - Inserir um Produto")
    print("2 - Consultar um produto por código")
    print("3 - Consultar todos produtos")
    print("4 - Alterar preço/produto")
    print("5 - Aplicar acréscimo ou desconto / todos")
    print("6 - Salvar")
    print("7 - Excluir um Produto")
    print("8 - Sair")
    
    escolha = input("Escolha a opção (1-8): ")
    
    # Verifica se a entrada não está vazia e contém apenas dígitos
    if escolha.strip() and escolha.isdigit():
        opcao = int(escolha)
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 8.")
    
    # Opção 1: Inserir um novo produto no estoque
    if opcao == 1:
        print('-'*10)
        print("Cadastro")
        codigo = input('Digite o código: ')
        
        # Verifica se o produto já existe no estoque
        if codigo in banco_dados:
            print("Produto já inserido!")
        else:
            nome = input('Digite o nome do produto: ')
            preco = float(input("Digite o preço do kg/unidade: "))
            # Adiciona o novo produto ao dicionário "banco_dados"
            banco_dados[codigo] = {"nome": nome, "preco": preco}
    
    # Opção 2: Consulta um produto por código
    elif opcao == 2:
        print('-'*10)
        print("Consultar um produto por código")
        codigo = input('Digite o código do produto: ')
        
        # Verifica se o código existe no estoque
        if codigo in banco_dados:
            print(f"Nome: {banco_dados[codigo]['nome']}")
            print(f"Preço: {banco_dados[codigo]['preco']}")
        else:
            print("Produto não encontrado.")
    
    # Opção 3: Consulta todos os produtos
    elif opcao == 3:
        print('-'*10)
        print("Consultar todos produtos")
        if banco_dados:
            for codigo, produto in banco_dados.items():
                print(f"Código: {codigo}")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: {produto['preco']}")
                print("")
        else:
            print("Nenhum produto cadastrado.")
    
    # Opção 4: Altera o preço de um produto
    elif opcao == 4:
        print('-'*10)
        print("Alterar preço/produto")
        codigo = input('Digite o código do produto: ')
        
        # Verifica se o código existe no estoque
        if codigo in banco_dados:
            novo_preco = float(input('Digite o novo preço: '))
            # Atualiza o preço do produto no dicionário
            banco_dados[codigo]['preco'] = novo_preco
        else:
            print("Produto não encontrado.")
    
    # Opção 5: Aplica acréscimo ou desconto em todos os produtos
    elif opcao == 5:
        print('-'*10)
        print("Aplicar acréscimo ou desconto / todos")
        percentual = float(input("Digite o percentual de acréscimo (positivo) ou desconto (negativo): "))
        
        # Itera por todos os produtos no estoque
        for codigo, produto in banco_dados.items():
            # Atualiza o preço de cada produto com base no percentual
            produto['preco'] += produto['preco'] * (percentual / 100)
        
        print("Acréscimo ou desconto aplicado em todos os produtos.")
    
    # Opção 6: Salva os dados no arquivo JSON
    elif opcao == 6:
        print('-'*10)
        print("Salvando....")
        # Abre o arquivo "estoque.json" em modo de escrita ('w')
        with open("Projeto\estoque.json", 'w') as arquivo:
            # Salva o dicionário "banco_dados" de volta no arquivo JSON com formatação indentada
            json.dump(banco_dados, arquivo, indent=4)
    
    # Opção 7: Excluir um produto do estoque
    elif opcao == 7:
        print('-'*10)
        print("Excluir um Produto")
        codigo = input('Digite o código do produto a ser excluído: ')
        
        if codigo in banco_dados:
            # Confirmar a exclusão com o usuário
            confirmacao = input(f"Você tem certeza que deseja excluir o produto '{banco_dados[codigo]['nome']}' (S/N)? ").strip().lower()
            if confirmacao == 's':
                del banco_dados[codigo]
                print(f"Produto '{codigo}' excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
        else:
            # Se o código não existe, pedir ao usuário para tentar novamente ou voltar ao menu central
            while True:
                opcao_invalida = input("Produto não encontrado. Digite 'T' para tentar novamente ou 'M' para voltar ao menu central: ").strip().lower()
                if opcao_invalida == 't':
                    codigo = input('Digite o código do produto a ser excluído: ')
                    if codigo in banco_dados:
                        confirmacao = input(f"Você tem certeza que deseja excluir o produto '{banco_dados[codigo]['nome']}' (S/N)? ").strip().lower()
                        if confirmacao == 's':
                            del banco_dados[codigo]
                            print(f"Produto '{codigo}' excluído com sucesso.")
                        else:
                            print("Exclusão cancelada.")
                        break  # Sai do loop se o código for encontrado
                    else:
                        print("Produto não encontrado.")
                elif opcao_invalida == 'm':
                    break  # Sai do loop e volta ao menu central
                else:
                    print("Opção inválida. Digite 'T' para tentar novamente ou 'M' para voltar ao menu central.")

    
    # Opção 8: Sair do programa
    elif opcao == 8:
        print('-'*10)
        print("Saindo")
    
    # Opção inválida
    else:
        print('-'*10)
        print('Opção Inválida')

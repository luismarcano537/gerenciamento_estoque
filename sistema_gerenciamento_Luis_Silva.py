import time as tm

#Estrutura de dados para cadastro.
estoque = {}

#Algoritmo da função cadastrar produto. 
def cadastrar_produto(estoque):
    id_produto = len(estoque) +1 #Adiciona +1 dígito como ID do produto. 
    nome = input("\nDigite o nome do produto: ")
    categoria = input("Digite a categoria do produto ")

    while True: #Validar se o número inserido em quantidade é inteiro ou não.
        try:
            quantidade = int(input("Digite a quantidade em estoque: "))
            if quantidade < 0:
                print("A quantidade não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro.")

    while True: #Validar se o número inserido é decimal ou não.
        try:
            preco = float(input("Digite o preço do produto: "))
            if preco < 0:
                print("O preço não pode ser negativo, tente novamente.")
                continue
            break
        except ValueError:
            print("Valor inválido. Por favor, informe um número decimal.")

    localizacao = input("Digite a localização no depósito: ")

    estoque[id_produto] = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco,
        "localizacao": localizacao,
    }
    print(f"\nO produto '{estoque[id_produto]['nome']}' foi cadastrado com sucesso!\n")

#Algoritmo da função para consultar produtos.
def consultar_estoque(estoque):
    if not estoque:
        print("\nATENÇÃO: Estoque vazio!")
        return
    
    print("\nProdutos disponíveis no estoque:")
    for id_produto, info in estoque.items():
        print(f"\nID: {id_produto} | Nome: {info['nome']} | Categoria: {info['categoria']} | "
        f"Quantidade: {info['quantidade']} | Preço: R${info['preco']} | "
        f"Localização: {info['localizacao']}\n")
    
#Algoritmos de movimentação: funções para registrar entradas e saídas de produtos (Alterar estoque existente).

#Algoritmo da função para entrada de produtos.
def registrar_entrada(estoque):
    id_produto = int(input("\nDigite o ID do produto para registrar a entrada: "))
    if id_produto in estoque: #Estrutura de controle permite verificar se o produto existe. 
        quantidade = int(input("Digite a quantidade de entrada: "))
        estoque[id_produto]["quantidade"] += quantidade
        print(f"\n{quantidade} unidades adicionadas com sucesso em '{estoque[id_produto]['nome']}'.\n")
    else:
        print("\nATENÇÃO: Produto não encontrado!")

#Algoritmo para registrar saídas de produtos.
def registrar_saida(estoque):
    id_produto = int(input("\nDigite o ID do produto para realizar a saída: "))
    if id_produto in estoque:
        quantidade = int(input("Digite a quantidade a ser retirada: "))
        if quantidade <= estoque[id_produto]['quantidade']:
            estoque[id_produto]['quantidade'] -= quantidade
            print(f"\n{quantidade} unidades removidas do produto '{estoque[id_produto]['nome']}' no estoque.\n")
        else:
            print("\nAtenção: Quantidade de saída maior que o estoque disponível!\n")
    else:
        print("\nATENÇÃO: Produto não encontrado!\n")

#Algoritmo da função para localizar produtos no estoque.
def rastrear_localizacao(estoque):
    if not estoque:
        print("\nATENÇÃO: Estoque vazio, não há produtos disponíveis para rastrear.")
        return
    print("\nRastreamento de localização")
    opcao = input("\nDeseja buscar por (1) ID do produto ou (2) nome do produto? Digite 1 ou 2: ")

    if opcao == "1":
        try:
            id_produto = int(input("Digite o ID do produto: "))
            if id_produto in estoque:
                print(f"\n O produto '{estoque[id_produto]['nome']}' está localizado em: {estoque[id_produto]['localizacao']}")
            else:
                print("\nATENÇAO: Não foi possível localizar o produto a través do ID.")
        except ValueError:
            print("\nErro: Por favor, insira um número válido para o ID.")
    elif opcao == "2":
        nome_produto = input("Digite o nome do produto: ").lower()
        encontrado = False
        for id_produto, info in estoque.items():
            if info['nome'].lower() == nome_produto:
                print(f"\nO produto '{info['nome']}' está localizado em: {info['localizacao']}\n")
                encontrado = True
            break
        if not encontrado:
            print("\n ATENÇÃO: Produto com este nome não encontrado!\n")
    else:
        print("\nErro: Opção inválida!\n")

#Algoritmo para gerar relatórios sobre o status do estoque.
def gerar_relatorio(estoque):
    if not estoque:
        print("\nATENÇÃO: Estoque vazio, não é possível gerar o relatório!")
        return
    
    estoque_baixo = []
    estoque_alto = []

    print("\n--- Relatório de estoque ---")
    for id_produto, info in estoque.items():
        if info["quantidade"] < 100: #Verifica se o estoque está baixo.
            estoque_baixo.append((id_produto, info)) #Adiciona o item na lista estoque baixo.
        elif info["quantidade"] > 100: #Verifica se o estoque está com excesso.
            estoque_alto.append((id_produto, info))

    print("\nProdutos com estoque Baixo: ")
    for id_produto, info in estoque_baixo:
        print(f"ID: {id_produto} | Nome: {info['nome']} | Quantidade: {info['quantidade']}")

    print("\nProdutos com Excesso de Estoque: ")
    for id_produto, info in estoque_alto:
        print(f"ID: {id_produto} | Nome: {info['nome']} | Quantidade: {info['quantidade']}")

    print("\nResumo Geral: ")
    for id_produto, info in estoque.items():
        print(f"ID: {id_produto} | Nome: {info['nome']} | Quantidade: {info['quantidade']} | "
              f"Preço: {info['preco']:.2f} | Localização: {info['localizacao']}\n")

#Menu principal.
def menu():
    while True:
        print("=-=-=" * 10)
        print("Sistema de Gerenciamento de Estoque")
        print("=-=-=" * 10)
        print("1. Cadastrar produto")
        print("2. Consultar estoque (atualizar)")
        print("3. Registrar entrada de produtos")
        print("4. Registrar saída de produtos")
        print("5. Localizar produto")
        print("6. Gerar Relatórios do Estoque atual")
        print("0. Sair")
        opcao = input("\nDigite uma opção (Apenas número): ")

        if opcao == "1":
            cadastrar_produto(estoque)
            tm.sleep(2)
        elif opcao == "2":
            consultar_estoque(estoque)
            tm.sleep(2)
        elif opcao == "3":
            registrar_entrada(estoque)
            tm.sleep(2)
        elif opcao == "4":
            registrar_saida(estoque)
            tm.sleep(2)
        elif opcao == "5":
            rastrear_localizacao(estoque)
            tm.sleep(2)
        elif opcao == "6":
            gerar_relatorio(estoque)
            tm.sleep(2)
        elif opcao == "0":
            print("\nEncerrando sistema. Obrigado por ter utilizado o sistema de gerenciamento de estoque.")
            tm.sleep(2)
            print("\nSistema encerrado com sucesso. Caso precise de ajuda, entre em contato.\n")
            break
        else:
            print("\nOpção inválida. Tente novamente por favor.\n")

#Inciar o sistema.
menu()

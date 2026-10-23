import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

produtos = carregar_produtos()


def estoque():
    for lista in produtos:
     print (lista)

   
def pesquisa():
    pesquisar = (input("Informe o id ou nome: "))
    for lista in produtos:
     if str(lista["id"])  == pesquisar:
        print (lista)
     elif lista["nome"].lower() == pesquisar.lower():
        print (lista)

def alterar():
    a = input("Qual id deseja alterar?: ")

    for lista in produtos:
        if str(lista["id"]) == a:
           print(lista)
           produto = lista
           break
    
    while True:
        print(f"Produto selecionado: {produto}")
        print("1 - Alterar Nome")
        print("2 - Alterar Categoria")
        print("3 - Alterar o preço")
        print("4 - Alterar o estoque")
        print("0 - Salvar e Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo_nome = input("Digite o novo nome: ")
            produto["nome"] = novo_nome
            print("Nome atualizado!")

        elif opcao == "2":
            nova_cat = input("Digite a nova categoria: ")
            produto["categoria"] = nova_cat
            print("Categoria atualizada!")

        elif opcao == "3":
           nova_preco = float(input("Digite o novo preço: "))
           produto["preco"] = nova_preco
           print("Preço atualizada!")

        elif opcao == "4":
            novo_est = float(input("Digite a quantidade do estoque: "))
            produto["estoque"] = novo_est
            print("Preço atualizada!")

        elif opcao == "0":
            salvar_produtos(produtos)
            print("Alterações salvas com sucesso!")
            break  

        else:
            print("Opção inválida! Tente novamente.")
   

def add():
   novo_id = len(produtos) + 1 
   novo_nome = input("Qual é o nome?: ")
   novo_categoria = input("Qual é a categoria?: ")
   novo_preco = float(input("Qual é o preço?: "))
   novo_estoque = int(input("Qual é o número do estoque?: "))

   novo_produtos = {
      "id" : novo_id,
      "nome" : novo_nome,
      "categoria" : novo_categoria,
      "preco" : novo_preco,
      "estoque" : novo_estoque
   }

   produtos.append(novo_produtos)
   salvar_produtos(produtos)

def remover():
      dele = input("Qual id deseja remover?: ")
      for lista in produtos:
         if str(lista["id"]) == dele:
            produtos.remove(lista)
            salvar_produtos(produtos)
            return


while True:

    print ("1 - Mostrar estoque")
    print ("2 - Pesquisar produto")
    print ("3 - Alterar produto")
    print ("4 - Adicionar produto")
    print ("5 - Remover produto")
    print ("0 - Sair")

    opcao = input ("Escolhe uma opção: ")

    if opcao == "1":
       estoque()

    elif opcao == "2":
       pesquisa()

    elif opcao =="3":
       alterar()

    elif opcao == "4":
       add()

    elif opcao == "5":
       remover()

    
       

   
 
# Sistema de controle de estoque
print("=== Controle de estoque ===")

# Lista que armazenará os produtos
produtos= []

# Cadastro de 5 produtos
for i in range(5):
    print(f"\n--- cadastro do {i + 1}º produto ---")

    nome= input("Nome do produto: ")
    preco= float(input("Preço Unitário: ").replace(",", "."))
    quantidade= int(input("Quantidade em estoque: "))

    # Criação do dicionário do produto
    produto= {"nome": nome, "preco": preco, "quantidade": quantidade}

    # Adiciona o produto à lista
    produtos.append(produto)

# Calcula o valor total do estoque
valor_total= 0

for produto in produtos:
    valor_total+= produto["preco"] * produto["quantidade"]

# Encontra o produto com maior preço
produto_maior_preco= produtos[0]

for produto in produtos:
    if produto["preco"]> produto_maior_preco["preco"]:
        produto_maior_preco= produto

# Exibição dos produtos
print("\n" + "=" * 50)
print("             Produtos cadastrados")
print("=" * 50)

# Exibição dos resultados
print(f"Valor total do estoque: R$ {valor_total:.2f}")
print(f"Produto com maior preço: " f"{produto_maior_preco["nome"]} " f"R$ {produto_maior_preco["preco"]:.2f}")

print("=" * 50)
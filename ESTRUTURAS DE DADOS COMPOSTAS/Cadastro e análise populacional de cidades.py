# Cadastro e análise de cidades
print("=== Cadastro de cidades ===")

# Lista que armazenará as cidades
cidades= []

# Cadastro de 5 cidades
for i in range(5):
    print(f"\n--- Cadastro da {i + 1}ª cidade ---")

    nome= input("Nome da cidade: ")
    estado= input("Sigla do estado: ").upper()
    populacao= int(input("População estimada: "))

    # Criação do dicionário da cidade
    cidade= {"nome": nome, "estado": estado, "populacao": populacao}

    # Adiciona a cidade à lista
    cidades.append(cidade)

# Variáveis inicias
populacao_total= 0
maior_cidade= cidades[0]
menor_cidade= cidades[0]

# Percorre a lista para fazer os cálculos
for cidade in cidades:
    # Soma a população
    populacao_total+= cidade["populacao"]

    # Verifica a maior população
    if cidade["populacao"]> maior_cidade["populacao"]:
        maior_cidade= cidade

    # Verifica a menor população
    if cidade["populacao"]< menor_cidade["populacao"]:
        menor_cidade= cidade

# Calcula a média populacional
media_populacional= populacao_total/len(cidades)

# Exibição dos resultados
print("\n" + "=" * 50)
print("        Dados das cidades cadastradas")
print("=" * 50)

for cidade in cidades:
    print(f"Nome:       {cidade["nome"]}")
    print(f"Estado:     {cidade["estado"]}")
    print(f"População:  {cidade["populacao"]}")
    print("-" * 50)

print("\n=== Análise populacional ===")

print(f"Maior população: {maior_cidade["nome"]}" " | " f"{maior_cidade["estado"]}" " | " f"{maior_cidade["populacao"]}")

print(f"População total: {populacao_total}")
print(f"Média populacional: {media_populacional:.2f}")

print("=" * 50)
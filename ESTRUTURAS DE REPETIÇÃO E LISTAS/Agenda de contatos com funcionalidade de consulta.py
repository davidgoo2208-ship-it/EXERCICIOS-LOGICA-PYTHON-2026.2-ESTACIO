# Agenda eletrônica simples
contatos= []

# Cadastro de 5 contatos
for i in range(5):
    print(f"\n--- Cadastro do {i + 1}º contato ---")

    nome= input("Nome: ")
    telefone= input("Telefone: ")
    email= input("E-mail: ")

    contato= {"nome": nome, "telefone": telefone, "email": email}

    contatos.append(contato)

# Consulta de contato
print("\n=== Consulta de contato ===")
nome_consulta= input("Digite o nome da pessoa que deseja consultar: ")

encontrado= False

for contato in contatos:
    if contato["nome"].lower()== nome_consulta.lower():
        print("\n=== Contato encontrado ===")
        print(f"Nome: {contato["nome"]}")
        print(f"Telefone: {contato["telefone"]}")
        print(f"E-mail: {contato["email"]}")

        encontrado= True
        break

if not encontrado:
    print("Contato não encontrado")
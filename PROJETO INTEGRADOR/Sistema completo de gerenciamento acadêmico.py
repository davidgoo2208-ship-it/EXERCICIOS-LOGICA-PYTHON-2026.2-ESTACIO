# Sistema acadêmico
estudantes= []

# Tupla com as possíveis situações acadêmicas
Situacoes= ("Aprovado", "Recuperação", "Reprovado")

# Funções de validação
def ler_idade():
    """Solicita uma idade inteira e positiva."""
    while True:
        try:
            idade= int(input("Idade: "))

            if idade> 0:
                return idade
            else:
                print("A idade deve ser um número inteiro positivo.")

        except ValueError:
            print("Digite uma idade válida.")


def ler_nota(numero_nota):
    """Solicita uma nota entre 0 e 10."""
    while True:
        try:
            nota= float(input(f"Nota {numero_nota} (0 a 10): ").replace(",", "."))

            if 0<= nota<= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite uma nota válida.")

# Função para calcular média e situação
def calcular_media(notas):
    """Calcula a média das três notas."""
    return sum(notas)/len(notas)


def calcular_situacao(media):
    """Determina a situação acadêmica do estudante."""

    if media>= 7:
        return Situacoes[0] # Aprovado

    elif media>= 5:
        return Situacoes[1] # Recuperação

    else:
        return Situacoes[2] # Reprovado

# Cadastrar estudante
def cadastrar_estudante():
    print("\n=== Cadastrar estudante ===")

    nome= input("Nome: ").strip()
    idade= ler_idade()
    curso= input("Curso: ").strip()

    notas= []

    for i in range(1, 4):
        nota= ler_nota(i)
        notas.append(nota)

    media= calcular_media(notas)
    situacao= calcular_situacao(media)

    estudante= {"nome": nome,
                "idade": idade,
                "curso": curso,
                "notas": notas,
                "media": media,
                "situacao": situacao}


    estudantes.append(estudante)

    print("\nEstudante cadastrado com sucesso!")
    print(f"Média final: {media:.2f}")
    print(f"Situação: {situacao}")

# Listar estudantes
def listar_estudantes():
    print("\n=== Lista de estudantes ===")

    if len(estudantes)== 0:
        print("Nenhum estudante cadastrado.")
        return

    for i, estudante in enumerate(estudantes, start=1):
        print(f"\n--- Estudante {i} ---")
        print(f"Nome:       {estudante['nome']}")
        print(f"Idade:      {estudante['idade']}")
        print(f"Curso:      {estudante['curso']}")
        print(f"Notas:      {estudante['notas']}")
        print(f"Média:      {estudante['media']:.2f}")
        print(f"Situação:   {estudante['situacao']}")


# Buscar estudante
def buscar_estudante(nome):
    """Procura um estudante pelo nome."""

    for estudante in estudantes:
        if estudante["nome"].lower() == nome.lower():
            return estudante

    return None

# Consultar estudante
def consultar_estudante():
    print("\n=== Consultar estudante ===")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    nome= input("Digite o nome do estudante: ").strip()

    estudante= buscar_estudante(nome)

    if estudante is None:
        print("Estudante não encontrado.")
    else:
        print("\n=== Dados do estudante ===")
        print(f"Nome:       {estudante['nome']}")
        print(f"Idade:      {estudante['idade']}")
        print(f"Curso:      {estudante['curso']}")
        print(f"Nota 1:     {estudante['notas'][0]:.2f}")
        print(f"Nota 2:     {estudante['notas'][1]:.2f}")
        print(f"Nota 3:     {estudante['notas'][2]:.2f}")
        print(f"Média:      {estudante['media']:.2f}")
        print(f"Situação:   {estudante['situacao']}")

# Alterar dados
def alterar_dados():
    print("\n=== Alterar dados ===")

    if len(estudantes)== 0:
        print("Nenhum estudante cadastrado.")
        return

    nome_busca= input("Digite o nome do estudante: ").strip()

    estudante= buscar_estudante(nome_busca)

    if estudante is None:
        print("Estudante não encontrado.")
        return

    while True:
        print("\n=== Dados para alteração ===")
        print("1 - Alterar nome")
        print("2 - Alterar idade")
        print("3 - Alterar curso")
        print("4 - Alterar nota 1")
        print("5 - Alterar nota 2")
        print("6 - Alterar nota 3")
        print("0 - Voltar")

        opcao= input("Escolha uma opção: ")

        if opcao== "1":
            novo_nome= input("Novo nome: ").strip()

            if novo_nome!= "":
                estudante["nome"] = novo_nome
                print("Nome alterado com sucesso.")
            else:
                print("O nome não pode ficar vazio.")

        elif opcao== "2":
            estudante["idade"] = ler_idade()
            print("Idade alterada com sucesso.")

        elif opcao== "3":
            novo_curso= input("Novo curso: ").strip()

            if novo_curso!= "":
                estudante["curso"]= novo_curso
                print("Curso alterado com sucesso.")
            else:
                print("O curso não pode ficar vazio.")

        elif opcao== "4":
            estudante["notas"][0]= ler_nota(1)

            estudante["media"]= calcular_media(estudante["notas"])
            estudante["situacao"]= calcular_situacao(estudante["media"])

            print("Nota alterada com sucesso.")

        elif opcao== "5":
            estudante["notas"][1]= ler_nota(2)

            estudante["media"]= calcular_media(estudante["notas"])
            estudante["situacao"]= calcular_situacao(estudante["media"])

            print("Nota alterada com sucesso.")

        elif opcao== "6":
            estudante["notas"][2]= ler_nota(3)

            estudante["media"]= calcular_media(estudante["notas"])
            estudante["situacao"]= calcular_situacao(estudante["media"])

            print("Nota alterada com sucesso.")

        elif opcao== "0":
            break

        else:
            print("Opção inválida.")

# Remover estudante
def remover_estudante():
    print("\n=== Remover estudante ===")

    if len(estudantes)== 0:
        print("Nenhum estudante cadastrado.")
        return

    nome_busca= input("Digite o nome do estudante: ").strip()

    estudante= buscar_estudante(nome_busca)

    if estudante is None:
        print("Estudante não encontrado.")
        return

    print("\nEstudante encontrado:")
    print(f"Nome: {estudante['nome']}")
    print(f"Curso: {estudante['curso']}")

    confirmacao= input("Deseja realmente remover? (S/N): ").strip().lower()

    if confirmacao== "s":
        estudantes.remove(estudante)
        print("Estudante removido com sucesso.")
    else:
        print("Operação cancelada.")

# Relatório da turma
def gerar_relatorio():
    print("\n=== Relatório da turma ===")

    if len(estudantes)== 0:
        print("Nenhum estudante cadastrado.")
        return

    total= len(estudantes)

    maior= estudantes[0]
    menor= estudantes[0]

    soma_medias= 0

    aprovados= 0
    recuperacao= 0
    reprovados= 0

    for estudante in estudantes:

        media= estudante["media"]

        soma_medias+= media

        # Maior média
        if media> maior["media"]:
            maior= estudante

        # Menor média
        if media< menor["media"]:
            menor= estudante

        # Situação
        if media>= 7:
            aprovados+= 1

        elif media>= 5:
            recuperacao+= 1

        else:
            reprovados+= 1

    media_geral= soma_medias/total

    print(f"\nTotal de estudantes: {total}")

    print(
        f"Maior média: {maior['nome']} - "
        f"{maior['media']:.2f}"
    )

    print(
        f"Menor média: {menor['nome']} - "
        f"{menor['media']:.2f}"
    )

    print(f"Média geral da turma: {media_geral:.2f}")

    print(f"\nAprovados:    {aprovados}")
    print(f"Recuperação:  {recuperacao}")
    print(f"Reprovados:   {reprovados}")

# Menu principal
def menu():
    while True:

        print("\n========================================")
        print("          Sistema acadêmico")
        print("========================================")
        print("1 - Cadastrar estudante")
        print("2 - Listar estudantes")
        print("3 - Consultar estudante")
        print("4 - Alterar dados")
        print("5 - Remover estudante")
        print("6 - Gerar relatório da turma")
        print("0 - Encerrar sistema")
        print("========================================")

        opcao= input("Escolha uma opção: ")

        if opcao== "1":
            cadastrar_estudante()

        elif opcao== "2":
            listar_estudantes()

        elif opcao== "3":
            consultar_estudante()

        elif opcao== "4":
            alterar_dados()

        elif opcao== "5":
            remover_estudante()

        elif opcao== "6":
            gerar_relatorio()

        elif opcao== "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

# Início do programa
menu()
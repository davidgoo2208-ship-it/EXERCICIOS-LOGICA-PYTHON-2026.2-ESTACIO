# Sistemas de informações acadêmicas
estudantes= []

# Função para cadastrar um estudante
def cadastrar_estudante():
    nome= input("Nome do esudante: ")

    notas= []

    for i in range(3):
        while True:
            try:
                nota= float(input(f"Digite a {i + 1}ª nota (0 a 10): ").replace(",", "."))

                if 0<= nota<= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 a 10.")

            except ValueError:
                    print("Digite uma nota válida.")

    media= sum(notas)/3

    estudante= {"nome": nome, "notas": notas, "media": media}

    estudantes.append(estudante)

# Cadastrar 5 estudantes
for i in range(5):
     print(f"\n--- Cadastro do {i + 1}º estudante ---")
     cadastrar_estudante()

# Mostrar nome e média de cada estudante
def mostrar_medias():
     print("\n=== Médias dos estudantes ===")

     for estudante in estudantes:
          print(f"{estudante["nome"]}: {estudante["media"]:.2f}")

# Encontrar maior e menor média
def encontrar_maior_menor():
     maior= estudantes[0]
     menor= estudantes[0]

     for estudante in estudantes:
         if estudante["media"]> maior["media"]:
              maior= estudante

         if estudante["media"]< menor["media"]:
              menor= estudante

     return maior, menor

# Contar estudantes por situação
def contar_situacoes():
     aprovados= 0
     recuperacao= 0
     reprovados= 0

     for estudante in estudantes:
          media= estudante["media"]

          if media>= 7:
               aprovados+= 1

          elif media>= 5:
               recuperacao+= 1

          else:
               reprovados+= 1

     return aprovados, recuperacao, reprovados

# Exibir resultados
mostrar_medias()

maior, menor= encontrar_maior_menor()

aprovados, recuperacao, reprovados= contar_situacoes()

print("\n=== Destaques da turma ===")
print(f"Maior média: {maior["nome"]} - {maior["media"]:.2f}")
print(f"Menor média: {menor["nome"]} - {menor["media"]:.2f}")

print("\n=== Situação da turma ===")
print(f"Aprovados: {aprovados}")
print(f"Em recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")
# Sistema de avaliação de notas de estudantes
print("=== Sistema de notas ===")

# Entrada e verificação das notas
while True:
    nota1= float(input("Digite a primeira nota (entre 0 a 10): ").replace(",", "."))

    if 0 <= nota1 <= 10:
        break
    else:
        print("Erro: a nota deve estar entre 0 e 10. Tente novamente.")

while True:
    nota2= float(input("Digite a segunda nota (entre 0 a 10): ").replace(",", "."))

    if 0 <= nota2 <= 10:
        break
    else:
        print("Erro: a nota deve estar entre 0 e 10. Tente novamente.")

while True:
    nota3= float(input("Digite a terceira nota (entre 0 a 10): ").replace(",", "."))

    if 0 <= nota3 <= 10:
        break
    else:
        print("Erro: a nota deve estar entre 0 e 10. Tente novamente.")

# Cálculo da média
media= (nota1 + nota2 + nota3) / 3

# verificação da situação do estudante
if media >= 7:
    situacao= "Aprovado"
elif media >= 5:
    situacao= "Recuperação"
else:
    situacao= "Reprovado"

# Exibição do resultado
print("\n" + "=" * 40)
print("     === Resultado do estudante ===")
print("=" * 40)

print(f"Nota 1:    {nota1:.2f}")
print(f"Nota 2:    {nota2:.2f}")
print(f"Nota 3:    {nota3:.2f}")
print(f"Média:     {media:.2f}")
print(f"Situação:  {situacao}")

print("=" * 40)
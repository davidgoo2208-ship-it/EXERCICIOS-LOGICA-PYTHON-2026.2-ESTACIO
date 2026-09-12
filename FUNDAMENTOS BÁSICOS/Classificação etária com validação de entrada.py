# Classificador de faixa etária
print("=== Classificação Etária ===")

# Validação de entrada para idade
while True:
    try:
        idade= int(input("Digite a idade da pessoa: "))

        if idade>= 0:
            break
        else:
            print("Erro: a idade não pode ser negativa. Tente novamente.")
    except ValueError:
        print("Erro: digite uma idade válida.")

# Classificação da idade recebida
if idade<= 12:
    classificacao= "Criança"
elif 13 <=idade<= 17:
    classificacao= "Adolescente"
elif 18 <=idade<= 59:
    classificacao= "Adulto"
elif idade>= 60:
    classificacao= "Idoso"

# Resultado da classificação
print("\n" + "=" * 35)
print("=== Resultado da classificação ===")
print("=" * 35)
print(f"Idade: {idade} anos")
print(f"Classificação: {classificacao}")
print("=" * 35)
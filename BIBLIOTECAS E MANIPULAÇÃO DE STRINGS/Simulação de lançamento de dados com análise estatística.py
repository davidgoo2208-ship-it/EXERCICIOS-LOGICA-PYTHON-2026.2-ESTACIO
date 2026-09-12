# Simulador de lançamento de dados
import random

# Parte 1 - Lançamento único

dado1= random.randint(1, 6)
dado2= random.randint(1, 6)

soma= dado1 + dado2

# Resultado do lançamento único
print("=== Lançamento único ===")
print(f"Primeiro dado: {dado1}")
print(f"Segundo dado:  {dado2}")
print(f"Soma:          {soma}")


# Parte 2 - 10 lançamentos

quantidade_sete= 0

print("\n=== 10 Lançamentos ===")

for i in range(10):
    dado1= random.randint(1, 6)
    dado2= random.randint(1, 6)

    soma= dado1 + dado2

# Resultados dos 10 lançamentos
    print(
        f"Lançamento {i + 1}: "
        f"Dado 1 = {dado1}, "
        f"Dado 2 = {dado2}, "
        f"Soma = {soma}"
    )

# Quantidade de vezes que a soma deu 7
    if soma== 7:
        quantidade_sete+= 1

print(f"\nA soma foi igual a 7 em {quantidade_sete} lançamento(s).")
# Relatório estatístico de 10 números inteiros
print("=== Relatório estatístico ===")

# Variáveis para armazenar os resultados
soma= 0
positivos= 0
negativos= 0
pares= 0
impares= 0

# Repetição para receber os 10 números
for i in range(10):
    numero= int(input(f"Digite o {i + 1}º número inteiro: "))

    # Soma
    soma+= numero

    # Positivo ou negativo
    if numero> 0:
        positivos+= 1
    elif numero< 0:
        negativos+= 1

    # Par ou ímpar
    if numero% 2== 0:
        pares+= 1
    else:
        impares+= 1

# Cálculo da média
media= soma/10

# Exibição do relatório
print("\n" + "=" * 40)
print("        Relatório estatístico")
print("=" * 40)

print(f"soma:                {soma}")
print(f"Números positivos:   {positivos}")
print(f"Números negativos:   {negativos}")
print(f"Números pares:       {pares}")
print(f"Números ímpares:     {impares}")
print(f"Média aritmética:    {media:.2f}")

print("=" * 40)
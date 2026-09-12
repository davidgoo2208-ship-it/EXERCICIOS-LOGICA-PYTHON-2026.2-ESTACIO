# Relatório de 10 números inteiros
print("=== Relatório de números ===")

# Listas
numeros= []
pares= []
impares= []

# Entrada dos 10 números
for i in range(10):
    numero= int(input(f"Digite o {i + 1}º número inteiro: "))

    # Armazena o número na lista principal
    numeros.append(numero)

    # Verifica se é par ou ímpar
    if numero% 2==0:
        pares.append(numero)
    else:
        impares.append(numero)

# Cálculos
soma= sum(numeros)
media= soma/len(numeros)
maior= max(numeros)
menor= min(numeros)

# Exibição do relatório
print("\n" + "=" * 45)
print("           Relatório")
print("=" * 45)

print(f"Números informados:  {numeros}")
print(f"Números pares:       {pares}")
print(f"Números ímpares:     {impares}")
print(f"Soma dos valores:    {soma}")
print(f"Média dos valores:   {media:.2f}")
print(f"Maior valor:         {maior}")
print(f"Menor valor:         {menor}")

print("=" * 45)
# Comparador manual de três números inteiros
print("=== Comparação de números ===")

# Entrada dos números 
numero1= int(input("Digite o primeiro número inteiro: "))
numero2= int(input("Digite o segundo número inteiro: "))
numero3= int(input("Digite o terceiro número inteiro: "))

# Verificação do maior e menor número
if numero1> numero2:
    if numero1> numero3:
        maior= numero1

        if numero2< numero3:
            menor= numero2
            mediana= numero3
        else:
            menor= numero3
            mediana= numero2

    else:
        maior= numero3
        menor= numero2
        mediana= numero1

else:
    if numero2> numero3:
        maior= numero2

        if numero1< numero3:
            menor= numero1
            mediana= numero3
        else:
            menor= numero3
            mediana= numero1

    else:
        maior= numero3
        menor= numero1
        mediana= numero2

# Exibição dos resultados
print("\n" + "=" * 40)
print("          Resultado")
print("=" * 40)
print(f"Maior número:      {maior}") 
print(f"Número mediano:    {mediana}")
print(f"Menor número:      {menor}")
print("=" * 40)
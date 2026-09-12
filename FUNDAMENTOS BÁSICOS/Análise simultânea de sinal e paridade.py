# Verificação de sinal e paridade de um número
print("=== Análise do número ===")

# Entrada do número
numero= int(input("Digite um número inteiro: "))

# Verificação de positivo, negativo ou nulo
if numero> 0:
    sinal= "positivo"

elif numero< 0:
    sinal= "negativo"

else:
    sinal= "nulo"

# Verificação de par ou ímpar
if numero% 2 == 0:
    paridade= "par"
else:
    paridade= "ímpar"

# Exibição do resultado
print("\n" + "=" * 35)
print(f"O número {numero} é {sinal} e {paridade}.")
print("=" * 35)
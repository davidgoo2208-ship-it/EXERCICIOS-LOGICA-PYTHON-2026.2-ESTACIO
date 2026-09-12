# Cálculos matemáticos com módulo math
import math

# Solicita um número real
numero= float(input("Digite um número real: ").replace(",", "."))

# Raiz quadrada
if numero>= 0:
    raiz= math.sqrt(numero)
else:
    raiz= "Não existe raiz quadrada real."

# Valor absoluto
absoluto= math.fabs(numero)

# Arredondamento para cima
teto= math.ceil(numero)

# Arredondamento para baixo
piso= math.floor(numero)

# Exibição dos resultados
print("\n=== Informações matemáticas ===")

print(f"Número:                {numero}")
print(f"Raiz quadrada:         {raiz}")
print(f"Valor absoluto:        {absoluto}")
print(f"Arredondamento cima:   {teto}")
print(f"Arredondamento baixo:  {piso}")

# Fatorial
if numero.is_integer() and numero>= 0:
    fatorial= math.factorial(int(numero))
    print(f"Fatorial:              {fatorial}")
else:
    print("Fatorial:            Não é possível calcular o fatorial.")
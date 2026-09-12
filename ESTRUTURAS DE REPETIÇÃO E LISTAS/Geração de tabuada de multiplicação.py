# Tabuada de multiplicação
print("=== Tabuada ===")

# Entrada do número
numero= int(input("Digite um número inteiro: "))

# Exibição da tabuada
for i in range(1,11):
    resultado= numero * i
    print(f"{numero} x {i} = {resultado}")
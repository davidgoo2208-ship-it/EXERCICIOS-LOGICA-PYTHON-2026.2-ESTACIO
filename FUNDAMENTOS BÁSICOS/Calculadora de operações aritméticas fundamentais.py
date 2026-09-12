# Calculadora de dois números reais em todas as operações fundamentais
print("=== Calculadora ===")

# Entrada pra colocar os dois números
numero1= float(input("Digite o primeiro número: ").replace(",", "."))
numero2= float(input("Digite o segundo número: ").replace(",", "."))

# Operações que devem ser realizadas como esses números
adicao= numero1 + numero2
subtracao= numero1 - numero2
multiplicacao= numero1 * numero2
potenciacao= numero1 ** numero2

# Resultado dessas operações
print("\n" + "=" * 42)
print("         Resultados:")
print("=" * 42)

print(f"adição:         {adicao}")
print(f"subtração:      {subtracao}")
print(f"multiplicação:  {multiplicacao}")

# Verificação caso tenha uma divisão por zero
if numero2== 0:
    print("divisão:        Divisão por zero não é permitida.")
    print("divisão inteira: Divisão por zero não é permitida.")
    print("resto da divisão:", "não calculado.")

# O resto das operações 
else:
    divisao= numero1 / numero2
    divisao_inteira= numero1 // numero2
    resto= numero1 % numero2

    print(f"divisão:        {divisao}")
    print(f"divisão inteira: {divisao_inteira}")
    print(f"resto da divisão: {resto}")

print(f"potenciação:    {potenciacao}")

print("=" * 42)
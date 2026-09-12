# Cadastro de identificação pessoal
print("=== Cadastro de identificação ===")

# Nome completo
nome= input("Digite seu nome: ")

# Validação da idade
while True:
    try:
        idade= int(input("Digite sua idade: "))
        if idade>= 0:
            break
        else:
            print("Idade inválida. Por favor, digite um número não negativo.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Validação da altura
while True:
    try:
        altura= float(input("Digite sua altura em metros: ").replace(",", "."))
        if altura> 0:
            break
        else:
            print("Erro: a altura tem que ser maior que zero.")
    except ValueError:
        print("Erro: digite uma altura válida.")

# Cidade
Cidade= input("Digite a cidade onde reside: ")

# Exibição do cartão de identificação
print("\n" + "=" * 42)
print("         Cartão de identificação")
print("=" * 42)
print(f"{'nome completo': <18} {nome}")
print(f"{'idade': <18} {idade} anos")
print(f"{'altura': <18} {altura:.2f} m")
print(f"{'cidade': <18} {Cidade}")
print("=" * 42)
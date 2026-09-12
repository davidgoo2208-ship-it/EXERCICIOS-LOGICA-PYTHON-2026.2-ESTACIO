# Gerenciamento de números
numeros= []

while True:

    print("\n================================")
    print("    Gerenciamento de números")
    print("================================")
    print("1 - Cadastrar número")
    print("2 - Listar números")
    print("3 - Exibir maior número")
    print("4 - Exibir menor número")
    print("5 - Calcular média")
    print("0 - Encerrar programa")
    print("================================")

    opcao= input("Escolha uma opção: ")

    # 1 - Cadastrar número
    if opcao== "1":
        numero= float(input("Digite um número: ").replace(",", "."))
        numeros.append(numero)

        print("Número cadastrado com sucesso.")

    # 2 - Listar números
    elif opcao== "2":
        if len(numeros)== 0:
            print("Nenhum número cadastrado.")
        else:
            print("\n=== Números cadastrados ===")

            for i in range(len(numeros)):
                print(f"{i + 1} - {numeros[i]}")

    # 3 - Exibir maior número
    elif opcao== "3":
        if len(numeros)== 0:
            print("Nenhum número cadastrado.")
        else:
            maior= max(numeros)
            print(f"Maior número: {maior}")

    # 4 - Exibir menor número
    elif opcao== "4":
        if len(numeros)== 0:
            print("Nenhum número cadastrado.")
        else:
            menor= min(numeros)
            print(f"Menor número: {menor}")

    # 5 - Calcular média
    elif opcao == "5":
        if len(numeros)== 0:
            print("Nenhum número cadastrado.")
        else:
            media= sum(numeros) / len(numeros)
            print(f"Média: {media:.2f}")

    # 0 - Encerrar
    elif opcao== "0":
        print("Programa encerrado.")
        break

    # Opção inválida
    else:
        print("Opção inválida. Tente novamente.")
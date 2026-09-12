# Analisador de frase

frase= input("Digite uma frase: ")

# Remove espaços do início e do final
frase_limpa= frase.strip()

# Separa a frase em palavras
palavras= frase_limpa.split()

# Quantidade de caracteres, incluindo espaços
quantidade_caracteres= len(frase)

# Quantidade de palavras
quantidade_palavras= len(palavras)

# Primeira e última palavra
if quantidade_palavras > 0:
    primeira_palavra = palavras[0]
    ultima_palavra = palavras[-1]
else:
    primeira_palavra= "Nenhuma"
    ultima_palavra= "Nenhuma"

# Letra escolhida pelo usuário
letra= input("Digite uma letra para pesquisar: ")

# Conta as ocorrências da letra, ignorando maiúsculas/minúsculas
quantidade_letra = frase_limpa.lower().count(letra.lower())

# Exibição dos resultados
print("\n=== Análise de frase ===")
print(f"Quantidade de caracteres: {quantidade_caracteres}")
print(f"Quantidade de palavras:   {quantidade_palavras}")
print(f"Primeira palavra:         {primeira_palavra}")
print(f"Última palavra:           {ultima_palavra}")
print(f"Ocorrências de '{letra}':       {quantidade_letra}")
print(f"Frase em maiúsculas:      {frase_limpa.upper()}")
print(f"Frase em minúsculas:      {frase_limpa.lower()}")
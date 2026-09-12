# Análise das temperaturas de 7 dias
print("=== Estação meteorológica ===")

# Lista para armazenar as temperaturas
temperaturas= []

# Entrada das 7 temperaturas
for i in range(7):
    temperatura= float(input(f"Digite a temperatura do {i + 1}º dia: ").replace(",", "."))
    temperaturas.append(temperatura)

# Maior e menor temperatura
maior= max(temperaturas)
menor= min(temperaturas)

# Cálculo da média
soma= sum(temperaturas)
media= soma/7

# Contagem de temperatura acima da média
acima_media= 0

for temperatura in temperaturas:
    if temperatura> media:
        acima_media+= 1

# Exibição dos resultados
print("\n" + "=" * 45)
print("       Relatório meteorológico")
print("=" * 45)

print("Temperaturas registradas:")

for i in range(7):
    print(f"Dia {i + 1}: {temperaturas[i]:.2f} °C")

print("-" * 45)
print(f"Maior temperatura:   {maior:.2f} °C")
print(f"Menor temperatura:   {menor:.2f} °C")
print(f"Temperatura média:   {media:.2f} °C")
print(f"Dias acima da média: {acima_media}")

print("=" * 45)
# Conversão entre escalas de temperatura
print("=== Conversor de temperatura ===")

# Entrada da temperatura em Celsius
celsius= float(input("Digite a temperatura em Celsius: ").replace(",", "."))

# Conversões para as outras escalas
fahreinheit= (celsius * 9/5) + 32
kelvin= celsius + 273.15

# Resultado das conversões
print("\n" + "=" * 40)
print("       Resultados das conversões")
print("=" * 40)

print(f"Celsius:    {celsius:.2f} °C")
print(f"Fahrenheit: {fahreinheit:.2f} °F")
print(f"Kelvin:     {kelvin:.2f} K")

print("=" * 40)
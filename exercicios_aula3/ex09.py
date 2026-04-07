codigo_estado = int(input("Digite o código do estado de origem (1 a 5): "))
peso_toneladas = float(input("Digite o peso da carga em toneladas: "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

# peso para quilos
peso_kg = peso_toneladas * 1000

# preço por kg
if 10 <= codigo_carga <= 20:
    preco_por_kg = 100
elif 21 <= codigo_carga <= 30:
    preco_por_kg = 250
elif 31 <= codigo_carga <= 40:
    preco_por_kg = 340
else:
    preco_por_kg = 0  # Caso não esteja dentro dos intervalos válidos (segundo o enunciado, não ocorre)

# preço da carga
preco_carga = peso_kg * preco_por_kg

# imposto
if codigo_estado == 1:
    imposto = preco_carga * 0.35
elif codigo_estado == 2:
    imposto = preco_carga * 0.25
elif codigo_estado == 3:
    imposto = preco_carga * 0.15
elif codigo_estado == 4:
    imposto = preco_carga * 0.05
elif codigo_estado == 5:
    imposto = 0
else:
    imposto = 0

#total transportado
valor_total = preco_carga + imposto

print(f"\nPeso da carga em kg: {peso_kg:.2f} kg")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Valor do imposto: R$ {imposto:.2f}")
print(f"Valor total transportado: R$ {valor_total:.2f}")
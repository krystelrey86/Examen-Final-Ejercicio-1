# 1. Pedir los datos al usuario.
precio = float(input("Ingrese el precio del videojuego (Q): "))
es_vip = input("¿El cliente es miembro VIP? (si/no): ").strip().lower()

# 2. Aplicar la Regla 1: Descuento por precio >= Q500 (10%).
if precio >= 500:
    precio_actual = precio * 0.90
else:
    precio_actual = precio

# 3. Aplicar la Regla 2: Descuento adicional por ser VIP (15%).
if es_vip == "si":
    precio_final = precio_actual * 0.85
else:
    precio_final = precio_actual

# 4. Mostrar el resultado final.
print(f"El precio final a pagar es: Q{precio_final:.2f}")
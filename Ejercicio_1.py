def procesar_inventario(lista_productos):
    pedidos_urgentes = []
    valor_total_inventario = 0.0
    
    for producto in lista_productos:
        # 1. Identificar productos con poco stock
        if producto['stock'] < 5:
            pedidos_urgentes.append(producto['nombre'])
        # 2. Calcular valor total (Cantidad * Precio)
        valor_total_inventario += producto['stock'] * producto['precio']
        # 3. Aplicar "Descuento" (etiqueta Premium si cuesta más de 100)
        if producto['precio'] > 100:
            producto['tipo'] = "Premium"
        else:
            producto['tipo'] = "Estándar"  
    # Retorno de el informe rápido
    informe = {
        "pedidos_urgentes": pedidos_urgentes,
        "valor_total": valor_total_inventario,
        "inventario_actualizado": lista_productos
    }
    return informe

# --- Ejemplo de uso ---
inventario_ejemplo = [
    {"nombre": "Teclado", "stock": 2, "precio": 37.0},
    {"nombre": "Monitor 4K", "stock": 20, "precio": 406.0},
    {"nombre": "Mousepad", "stock": 10, "precio": 15.0},
    {"nombre": "Audífonos Premium", "stock": 3, "precio": 110.0}
]
resultado = procesar_inventario(inventario_ejemplo)
# Imprimir los resultados
print("Pedidos Urgentes:", ", ".join(resultado["pedidos_urgentes"]))
print(f"Valor Total del Inventario: Q{resultado['valor_total']}")
print("Lista de productos final:")
for prod in resultado["inventario_actualizado"]:
    print(f"- Producto: {prod['nombre']} | Stock: {prod['stock']} | Precio: Q{prod['precio']} | Tipo: {prod['tipo']}")
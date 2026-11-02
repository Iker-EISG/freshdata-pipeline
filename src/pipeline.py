def cargar_ventas(archivo):
    print(f"Cargando ventas desde: {archivo}")

    ventas = [
        {"tienda": "T001", "producto": "Leche", "cantidad": 150, "precio": 1.20},
        {"tienda": "T001", "producto": "Pan", "cantidad": 200, "precio": 0.80},
        {"tienda": "T002", "producto": "Leche", "cantidad": 90, "precio": 1.20},
        {"tienda": "T002", "producto": "Huevos", "cantidad": 75, "precio": 2.50},
    ]
    return ventas

def calcular_total_tiendas(ventas, tienda_id, con_iva=True):
    total = 0
    for venta in ventas:
        if venta["tienda"] == tienda_id:
            total += venta["cantidad"] * venta["precio"]
        if con_iva:
            from config import IVA
            total *= (1 + IVA)
            return total
        
if __name__ == "__main__":
    ventas = cargar_ventas("venttas_2026_01.csv")
    total = calcular_total_tiendas(ventas, "T001")
    print(f"Total tienda T001: ${total:.2f}")
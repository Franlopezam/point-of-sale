from dataclasses import dataclass
from datetime import datetime

@dataclass
class Producto:
    nombre: str
    precio: float

productos = {
    1: Producto("Hamburguesa", 85),
    2: Producto("Papas", 45),
    3: Producto("Refresco", 30),
    4: Producto("Combo", 130),
}

def mostrar_menu():
    for codigo, p in productos.items():
        print(f"{codigo}. {p.nombre} - ${p.precio:.2f}")

def vender():
    carrito = []
    while True:
        mostrar_menu()
        op = input("Código (0 termina): ").strip()
        if op == "0":
            break
        if not op.isdigit() or int(op) not in productos:
            print("Producto inválido")
            continue
        p = productos[int(op)]
        carrito.append(p)
        print(f"Agregado: {p.nombre}")

    total = sum(p.precio for p in carrito)
    print("\n--- TICKET ---")
    for p in carrito:
        print(f"{p.nombre:20} ${p.precio:7.2f}")
    print(f"TOTAL{' ':15} ${total:7.2f}")
    print("Fecha:", datetime.now().strftime("%d/%m/%Y %H:%M"))

if __name__ == "__main__":
    vender()

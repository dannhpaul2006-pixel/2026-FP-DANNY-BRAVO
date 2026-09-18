def calcularTotal(precio, cantidad):
    total = precio * cantidad
    return total

if __name__ == "__main__":
    precio = 15
    cantidad = 4
    resultado = calcularTotal(precio, cantidad)
    print(f"El total a pagar es: ${resultado}")
def calcular_area(base, altura):
    area = base * altura
    return area

# Programa principal
b = float(input("Ingrese la base del rectángulo: "))
h = float(input("Ingrese la altura del rectángulo: "))

resultado = calcular_area(b, h)
print(f"El área del rectángulo es: {resultado}")

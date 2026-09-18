asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print("--- Primera reserva ---")
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

if 0 <= fila <= 2 and 0 <= columna <= 3:
    if asientos[fila][columna] == 1:
        print("Este asiento ya está reservado.")
    else:
        asientos[fila][columna] = 1
        print("Asiento reservado con éxito.")
else:
    print("Fila o columna no válidas.")

print("\n--- Segunda reserva ---")
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

if 0 <= fila <= 2 and 0 <= columna <= 3:
    if asientos[fila][columna] == 1:
        print("Este asiento ya está reservado.")
    else:
        asientos[fila][columna] = 1
        print("Asiento reservado con éxito.")
else:
    print("Fila o columna no válidas.")

print("\nEstado de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end="  ")
    print()

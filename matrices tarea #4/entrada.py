
def ingresar_matriz():
    try:
        filas = int(input("Ingrese el número de filas: "))
        columnas = int(input("Ingrese el número de columnas: "))

        if filas <= 0 or columnas <= 0:
            print("Error: las dimensiones deben ser números enteros positivos.")
            return None

        matriz = []
        for i in range(filas):
            while True:
                try:
                    fila_str = input(f"Ingrese los elementos de la fila {i+1} separados por espacios: ").split()
                    if len(fila_str) != columnas:
                        print(f"Error: debe ingresar exactamente {columnas} elemento(s).")
                        continue
                    fila = [float(x) for x in fila_str]
                    matriz.append(fila)
                    break
                except ValueError:
                    print("Error: ingrese solo números en cada fila.")
        return matriz

    except ValueError:
        print("Error: las dimensiones deben ser números enteros.")
        return None


def mostrar_matriz(A):
    if A is None:
        print("No hay matriz para mostrar.")
        return
    for fila in A:
        fila_formateada = [f"{x:.2f}" if x != int(x) else str(int(x)) for x in fila]
        print("  [ " + "  ".join(fila_formateada) + " ]")

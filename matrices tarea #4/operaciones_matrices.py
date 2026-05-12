
def sumar_matrices(A, B):
    filasA, colsA = len(A), len(A[0])
    filasB, colsB = len(B), len(B[0])

    if filasA != filasB or colsA != colsB:
        print(f"Error: para sumar, ambas matrices deben tener las mismas dimensiones.")
        print(f"  Matriz A: {filasA}x{colsA}   Matriz B: {filasB}x{colsB}")
        return None

    resultado = []
    for i in range(filasA):
        fila = []
        for j in range(colsA):
            fila.append(A[i][j] + B[i][j])
        resultado.append(fila)
    return resultado


def multiplicar_matrices(A, B):
    filasA, colsA = len(A), len(A[0])
    filasB, colsB = len(B), len(B[0])

    if colsA != filasB:
        print(f"Error: las columnas de A deben ser iguales a las filas de B.")
        print(f"  Matriz A: {filasA}x{colsA}   Matriz B: {filasB}x{colsB}")
        return None

    resultado = []
    for i in range(filasA):
        fila = []
        for j in range(colsB):
            suma = 0
            for k in range(colsA):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado


def hadamard_matrices(A, B):
    filasA, colsA = len(A), len(A[0])
    filasB, colsB = len(B), len(B[0])

    if filasA != filasB or colsA != colsB:
        print(f"Error: para Hadamard, ambas matrices deben tener las mismas dimensiones.")
        print(f"  Matriz A: {filasA}x{colsA}   Matriz B: {filasB}x{colsB}")
        return None

    resultado = []
    for i in range(filasA):
        fila = []
        for j in range(colsA):
            fila.append(A[i][j] * B[i][j])
        resultado.append(fila)
    return resultado


def kronecker(A, B):
    filasA, colsA = len(A), len(A[0])
    filasB, colsB = len(B), len(B[0])

    filas_resultado = filasA * filasB
    cols_resultado  = colsA * colsB
    resultado = [[0.0] * cols_resultado for _ in range(filas_resultado)]

    for i in range(filasA):
        for j in range(colsA):
            for p in range(filasB):
                for q in range(colsB):
                    resultado[i * filasB + p][j * colsB + q] = A[i][j] * B[p][q]
    return resultado

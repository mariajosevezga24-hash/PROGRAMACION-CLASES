
from menu import mostrar_menu
from entrada import ingresar_matriz, mostrar_matriz
from operaciones_matrices import sumar_matrices, multiplicar_matrices, hadamard_matrices, kronecker


def pedir_dos_matrices():
    print("\nIngrese la Matriz A:")
    A = ingresar_matriz()
    if A is None:
        return None, None
    print("\nIngrese la Matriz B:")
    B = ingresar_matriz()
    if B is None:
        return None, None
    return A, B


def main():
    print("=== CALCULADORA DE OPERACIONES CON MATRICES ===")

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            print("\n--- SUMA DE MATRICES ---")
            A, B = pedir_dos_matrices()
            if A is None or B is None:
                continue
            resultado = sumar_matrices(A, B)
            if resultado is not None:
                print("\nMatriz A:");      mostrar_matriz(A)
                print("Matriz B:");        mostrar_matriz(B)
                print("Resultado A + B:"); mostrar_matriz(resultado)

        elif opcion == 2:
            print("\n--- MULTIPLICACIÓN DE MATRICES ---")
            A, B = pedir_dos_matrices()
            if A is None or B is None:
                continue
            resultado = multiplicar_matrices(A, B)
            if resultado is not None:
                print("\nMatriz A:");      mostrar_matriz(A)
                print("Matriz B:");        mostrar_matriz(B)
                print("Resultado A x B:"); mostrar_matriz(resultado)

        elif opcion == 3:
            print("\n--- PRODUCTO DE HADAMARD ---")
            A, B = pedir_dos_matrices()
            if A is None or B is None:
                continue
            resultado = hadamard_matrices(A, B)
            if resultado is not None:
                print("\nMatriz A:");       mostrar_matriz(A)
                print("Matriz B:");         mostrar_matriz(B)
                print("Resultado A ⊙ B:");  mostrar_matriz(resultado)

        elif opcion == 4:
            print("\n--- PRODUCTO DE KRONECKER ---")
            A, B = pedir_dos_matrices()
            if A is None or B is None:
                continue
            resultado = kronecker(A, B)
            if resultado is not None:
                print("\nMatriz A:");       mostrar_matriz(A)
                print("Matriz B:");         mostrar_matriz(B)
                print("Resultado A ⊗ B:");  mostrar_matriz(resultado)

        elif opcion == 5:
            print("\nFin del programa. ¡Hasta luego!")
            break


main()

# Programa con menú: conversión Celsius->Fahrenheit y tabla de multiplicar

def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def mostrar_tabla(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def pedir_opcion():
    print("\nMenú:")
    print("1) Conversión de temperatura")
    print("2) Tabla de multiplicar")
    print("3) Salir")
    return input("Elige una opción (1-3): ")

def main():
    while True:
        opcion = pedir_opcion().strip()
        if opcion == "1":
            try:
                c = float(input("Introduce grados Celsius (decimal permitido): ").strip())
            except ValueError:
                print("Entrada no válida: introduce un número decimal válido.")
            else:
                f = celsius_a_fahrenheit(c)
                print(f"{c} °C = {f:.2f} °F")
            input("Pulsa Enter para volver al menú...")
        elif opcion == "2":
            try:
                n = int(input("Introduce un entero para mostrar su tabla: ").strip())
            except ValueError:
                print("Entrada no válida: introduce un número entero.")
            else:
                print(f"Tabla de multiplicar de {n}:")
                mostrar_tabla(n)
            input("Pulsa Enter para volver al menú...")
        elif opcion == "3":
            print("Saliendo. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
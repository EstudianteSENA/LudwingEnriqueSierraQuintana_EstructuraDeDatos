# formulario.py
# Módulo de interfaz en consola que permite interactuar con el usuario

import base_datos

def pedir_par():
    """Solicita al usuario dos números enteros"""
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1, num2

def mostrar_menu():
    """Imprime el menú de opciones"""
    print(" \n --- MENÚ --- \n 1. Agregar nuevo par \n 2. Eliminar el último par (pop) \n 3. Insertar par en una posición específica \n 4. Eliminar un par específico (remove)") 
    print(" 5. Buscar índice de un par (index) \n 6. Mostrar todos los pares \n 7. Salir")

def main():
    """Punto de entrada principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            num1, num2 = pedir_par()
            base_datos.agregar_par(num1, num2)
            print("Par agregado exitosamente.")

        elif opcion == "2":
            eliminado = base_datos.eliminar_ultimo()
            if eliminado:
                print(f"Par eliminado: {eliminado}")
            else:
                print("La lista está vacía.")

        elif opcion == "3":
            try:
                posicion = int(input("Ingrese la posición en la que desea insertar: "))
                num1, num2 = pedir_par()
                if base_datos.insertar_en_posicion(posicion, num1, num2):
                    print("Par insertado correctamente.")
                else:
                    print("Posición inválida.")
            except ValueError:
                print("Entrada inválida. Ingrese solo números.")

        elif opcion == "4":
            num1, num2 = pedir_par()
            if base_datos.eliminar_par(num1, num2):
                print("Par eliminado exitosamente.")
            else:
                print("Par no encontrado en la lista.")

        elif opcion == "5":
            num1, num2 = pedir_par()
            indice = base_datos.buscar_par(num1, num2)
            if indice != -1:
                print(f"El par se encuentra en la posición: {indice}")
            else:
                print("Par no encontrado.")

        elif opcion == "6":
            pares = base_datos.obtener_lista()
            print("Lista actual de pares:")
            for i, par in enumerate(pares):
                print(f"{i}: {par}")

        elif opcion == "7":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

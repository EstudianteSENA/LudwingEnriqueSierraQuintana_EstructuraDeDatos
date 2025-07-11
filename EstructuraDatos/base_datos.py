# base_datos.py
# Módulo de gestión y manipulación de la base de datos de pares numéricos

# Lista general donde se almacenan los pares de números

lista_numeros = []

def agregar_par(num1, num2):
    """Agrega un par de números como sublista a la lista principal usando append()"""
    lista_numeros.append([num1, num2])

def eliminar_ultimo():
    """Elimina el último par ingresado usando pop()"""
    if lista_numeros:
        return lista_numeros.pop()
    else:
        return None

def insertar_en_posicion(posicion, num1, num2):
    """Inserta un par en una posición específica usando insert()"""
    if 0 <= posicion <= len(lista_numeros):
        lista_numeros.insert(posicion, [num1, num2])
        return True
    return False

def eliminar_par(num1, num2):
    """Elimina el primer par que coincida completamente usando remove()"""
    try:
        lista_numeros.remove([num1, num2])
        return True
    except ValueError:
        return False

def buscar_par(num1, num2):
    """Busca un par específico y devuelve su índice usando index()"""
    try:
        return lista_numeros.index([num1, num2])
    except ValueError:
        return -1

def obtener_lista():
    """Devuelve la lista completa de pares"""
    return lista_numeros

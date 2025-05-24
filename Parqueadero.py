import time
from datetime import datetime
from colorama import init, Fore, Back, Style

init(autoreset=True)

FILAS = 8
COLUMNAS = 8

parqueadero = [['L' for _ in range(COLUMNAS)] for _ in range(FILAS)]
vehiculos = {}

parqueadero[0][0] = 'E'
parqueadero[7][7] = 'S'

no_habilitadas = [(0, 6), (2, 5), (6, 6)]
for i, j in no_habilitadas:
    parqueadero[i][j] = 'V'

for i in range(1, FILAS-1):
    parqueadero[i][COLUMNAS-1] = 'D'

paredes = [(0, 2), (0, 3), (0, 4), (0, 5),
           (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
for i, j in paredes:
    parqueadero[i][j] = 'X'

vehiculos_iniciales = [
    ("ABC123", "normal", (2, 2)),
    ("XYZ789", "discapacidad", (3, 7)),
    ("LMN456", "normal", (5, 3))
]

for placa, tipo, (i, j) in vehiculos_iniciales:
    parqueadero[i][j] = 'OD' if tipo == 'discapacidad' else 'O'
    vehiculos[placa] = {
        'entrada': datetime.now(),
        'posicion': (i, j),
        'tipo': tipo
    }

def mostrar_mapa():
    print("\nMapa del Parqueadero:")
    for fila in parqueadero:
        for celda in fila:
            if celda == 'L':
                print(Fore.GREEN + 'L', end=' ')
            elif celda == 'O':
                print(Fore.RED + 'O', end=' ')
            elif celda == 'D':
                print(Fore.CYAN + 'D', end=' ')
            elif celda == 'OD':
                print(Fore.MAGENTA + 'DO', end=' ')
            elif celda == 'V':
                print(Fore.LIGHTYELLOW_EX + 'C', end=' ')
            elif celda == 'X':
                print(Fore.BLACK + 'X', end=' ')
            elif celda in ['E', 'S']:
                print(Fore.YELLOW + celda, end=' ')
            else:
                print(Fore.WHITE + celda, end=' ')
        print()
    print("\n")

def encontrar_espacio_libre(tipo):
    if tipo == 'discapacidad':
        for i in range(1, FILAS-1):
            if parqueadero[i][COLUMNAS-1] == 'D':
                return i, COLUMNAS-1
    else:
        for i in range(FILAS):
            for j in range(COLUMNAS):
                if parqueadero[i][j] == 'L':
                    return i, j
    return None

def ingresar_vehiculo(placa, tipo):
    disponibles = []
    print("Espacios disponibles para tu tipo de vehículo:")

    for i in range(FILAS):
        for j in range(COLUMNAS):
            if tipo == 'discapacidad' and parqueadero[i][j] == 'D':
                disponibles.append((i, j))
                print(f"  - Fila {i}, Columna {j}")
            elif tipo == 'normal' and parqueadero[i][j] == 'L':
                disponibles.append((i, j))
                print(f"  - Fila {i}, Columna {j}")

    if not disponibles:
        print("No hay espacios disponibles para este tipo de vehículo.")
        return

    try:
        i = int(input("Ingrese la fila donde desea estacionarse: "))
        j = int(input("Ingrese la columna donde desea estacionarse: "))
    except ValueError:
        print("Entrada inválida. Debe ingresar números.")
        return

    if (i, j) not in disponibles:
        print("La posición seleccionada no está disponible o no es válida para este tipo de vehículo.")
        return

    parqueadero[i][j] = 'OD' if tipo == 'discapacidad' else 'O'
    vehiculos[placa] = {
        'entrada': datetime.now(),
        'posicion': (i, j),
        'tipo': tipo
    }
    print(f"Vehículo {placa} ({tipo}) ingresado en la posición {i},{j}.")

def retirar_vehiculo(placa):
    if placa in vehiculos:
        i, j = vehiculos[placa]['posicion']
        tipo = vehiculos[placa]['tipo']
        parqueadero[i][j] = 'D' if tipo == 'discapacidad' else 'L'
        tiempo = datetime.now() - vehiculos[placa]['entrada']
        minutos = tiempo.total_seconds() / 60
        tarifa = calcular_tarifa(minutos)
        print(f"Vehículo {placa} retirado. Tiempo: {minutos:.2f} minutos. Total a pagar: ${tarifa:.2f}")
        del vehiculos[placa]
    else:
        print("Vehículo no encontrado.")

def calcular_tarifa(minutos):
    tarifa_por_minuto = 50
    return minutos * tarifa_por_minuto

def mostrar_disponibilidad():
    libres = sum(fila.count('L') for fila in parqueadero) + sum(fila.count('D') for fila in parqueadero)
    ocupados = sum(fila.count('O') for fila in parqueadero) + sum(fila.count('OD') for fila in parqueadero)
    print(f"Espacios libres: {libres} | Espacios ocupados: {ocupados}")

while True:
    mostrar_mapa()
    mostrar_disponibilidad()
    print("1. Ingresar vehículo")
    print("2. Retirar vehículo")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        placa = input("Ingrese la placa del vehículo: ")
        tipo = input("Tipo de vehículo (normal/discapacidad): ").lower()
        if tipo not in ['normal', 'discapacidad']:
            print("Tipo de vehículo inválido.")
        else:
            ingresar_vehiculo(placa, tipo)
    elif opcion == '2':
        placa = input("Ingrese la placa del vehículo a retirar: ")
        retirar_vehiculo(placa)
    elif opcion == '3':
        print("Saliendo del sistema.")
        break
    else:
        print("Opción inválida. Intente de nuevo.")

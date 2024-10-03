import csv

# Paso 1: Extraer datos del archivo CSV
with open('basket_players.csv', mode='r', encoding='ascii') as file:
    dades = csv.reader(file, delimiter=';')

    # Paso 2: Almacenar las filas y contar el número total de filas
    total_files = 0
    for i, fila in enumerate(dades):
        # Imprimir la fila
        print(f'Fila {i}: {fila}')
        total_files += 1

# Mostrar el número total de filas
print(f'Número total de filas: {total_files}')

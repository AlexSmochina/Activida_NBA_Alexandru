import csv

INCH_TO_CM = 2.54
POUND_TO_KG = 0.45

def leer_fitchero(filename):
    with open(filename, mode='r', encoding='ascii') as file:
        datos = csv.reader(file, delimiter=';')
        header = next(datos)
        return [fila for fila in datos]


def transformar(datos):

    column_dict = {
        'Name': 'Nom',
        'Team': 'Equip',
        'Position': 'Posicio',
        'Heigth': 'Altura',
        'Weigth': 'Pes',
        'Age': 'Edat'
    }

    position_dict = {
        "Point Guard": "Base",
        "Shooting Guard": "Escorta",
        "Small Forward": "Aler",
        "Power Forward": "Ala-pivot",
        "Center": "Pivot"
    }

    transformar_datos = []

    for fila in datos:

        nombre = fila[0]
        equipo = fila[1]
        pocision = position_dict[fila[2]]

        altura = round(float(fila[3]) * INCH_TO_CM, 2)
        peso = round(float(fila[4]) * POUND_TO_KG, 2)

        edad = round(float(fila[5]))

        transformar_datos.append([nombre, equipo, pocision, altura, peso, edad])

    return [list(column_dict.values())] + transformar_datos


def escribir_fitchero(data, filename):
    with open(filename, mode='w', encoding='ascii', newline='') as file:
        leer_datos = csv.writer(file, delimiter='^')
        leer_datos.writerows(data)


datos = leer_fitchero('basket_players.csv')
transformar_datos = transformar(datos)
escribir_fitchero(transformar_datos, 'jugadors_basket.csv')


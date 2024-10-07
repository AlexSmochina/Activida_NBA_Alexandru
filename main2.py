import csv

import matplotlib.pyplot as plt
import numpy as np

def leer_fitchero(filename):
    with open(filename, mode='r', encoding='ascii') as file:
        datos = csv.reader(file, delimiter='^')
        header = next(datos)
        data = [fila for fila in datos]
    return data


# Calcula estadístiques
def stadisticas(data):
    nombre = [fila[0] for fila in data]
    peso = [float(fila[4]) for fila in data]
    altura = [float(fila[3]) for fila in data]
    edad = [int(fila[5]) for fila in data]
    equipos = [fila[1] for fila in data]
    posicion = [fila[2] for fila in data]

    # a) Nom del jugador més pesat
    max_weight_name = nombre[peso.index(max(peso))]
    print(f'Jugador més pesat: {max_weight_name}')

    # b) Nom del jugador més baix
    min_height_name = nombre[altura.index(min(altura))]
    print(f'Jugador més baix: {min_height_name}')

    # c) Alçades en un diagrama de barres
    plt.bar(nombre, altura)
    plt.title('Alçades dels Jugadors')
    plt.ylabel('Alçada (cm)')
    plt.show()

    # d) Mitjana de pes i alçada per equip

    equipo_unico = set(equipos)
    avg_weights = [round(np.mean([peso[i] for i in range(len(peso)) if equipos[i] == equipo]), 2) for equipo in
                   equipo_unico]
    avg_heights = [round(np.mean([altura[i] for i in range(len(altura)) if equipos[i] == equipo]), 2) for equipo in
                   equipo_unico]

    plt.figure(figsize=(10, 5))
    bar_width = 0.35
    x = np.arange(len(equipo_unico))

    plt.bar(x, avg_weights, width=bar_width, label='Pes (kg)')
    plt.bar(x + bar_width, avg_heights, width=bar_width, label='Alçada (cm)')
    plt.title('Mitjana de Pes i Alçada per Equip')
    plt.xticks(x + bar_width / 2, equipo_unico)
    plt.legend()
    plt.show()

    # e) Recompte de jugadors per posició
    contador_posicion = {position: posicion.count(position) for position in set(posicion)}

    plt.figure(figsize=(8, 6))
    plt.pie(contador_posicion.values(), labels=contador_posicion.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Recompte de Jugadors per Posició')
    plt.show()

    # f) Distribució de jugadors per edat
    plt.figure(figsize=(10, 5))
    plt.hist(edad, bins=range(15, 40, 1), alpha=0.7, color='blue', edgecolor='black')
    plt.title('Distribució d\'Edat dels Jugadors')
    plt.xlabel('Edat')
    plt.ylabel('Nombre de Jugadors')
    plt.show()


# Execució de les estadístiques
data = leer_fitchero('jugadors_basket.csv')
stadisticas(data)

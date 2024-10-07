import csv

import matplotlib.pyplot as plt
import numpy as np

def load_statistics(filename):
    with open(filename, mode='r', encoding='ascii') as file:
        dades = csv.reader(file, delimiter='^')
        header = next(dades)
        data = [fila for fila in dades]
    return data


# Calcula estadístiques
def statistics(data):
    names = [fila[0] for fila in data]
    weights = [float(fila[4]) for fila in data]
    heights = [float(fila[3]) for fila in data]
    ages = [int(fila[5]) for fila in data]
    teams = [fila[1] for fila in data]
    positions = [fila[2] for fila in data]

    # a) Nom del jugador més pesat
    max_weight_name = names[weights.index(max(weights))]
    print(f'Jugador més pesat: {max_weight_name}')

    # b) Nom del jugador més baix
    min_height_name = names[heights.index(min(heights))]
    print(f'Jugador més baix: {min_height_name}')

    # c) Alçades en un diagrama de barres
    plt.bar(names, heights)
    plt.title('Alçades dels Jugadors')
    plt.ylabel('Alçada (cm)')
    plt.show()

    # d) Mitjana de pes i alçada per equip

    unique_teams = set(teams)
    avg_weights = [round(np.mean([weights[i] for i in range(len(weights)) if teams[i] == team]), 2) for team in
                   unique_teams]
    avg_heights = [round(np.mean([heights[i] for i in range(len(heights)) if teams[i] == team]), 2) for team in
                   unique_teams]

    plt.figure(figsize=(10, 5))
    bar_width = 0.35
    x = np.arange(len(unique_teams))

    plt.bar(x, avg_weights, width=bar_width, label='Pes (kg)')
    plt.bar(x + bar_width, avg_heights, width=bar_width, label='Alçada (cm)')
    plt.title('Mitjana de Pes i Alçada per Equip')
    plt.xticks(x + bar_width / 2, unique_teams)
    plt.legend()
    plt.show()

    # e) Recompte de jugadors per posició
    position_counts = {position: positions.count(position) for position in set(positions)}

    plt.figure(figsize=(8, 6))
    plt.pie(position_counts.values(), labels=position_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Recompte de Jugadors per Posició')
    plt.show()

    # f) Distribució de jugadors per edat
    plt.figure(figsize=(10, 5))
    plt.hist(ages, bins=range(15, 40, 1), alpha=0.7, color='blue', edgecolor='black')
    plt.title('Distribució d\'Edat dels Jugadors')
    plt.xlabel('Edat')
    plt.ylabel('Nombre de Jugadors')
    plt.show()


# Execució de les estadístiques
data = load_statistics('jugadors_basket.csv')
statistics(data)

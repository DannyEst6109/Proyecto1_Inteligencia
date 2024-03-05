import heapq
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Función para realizar Greedy Best-First Search en el contexto de un laberinto representado como una matriz
def greedy_best_first_search(labyrinth, start, goal, heuristic):
    rows, cols = len(labyrinth), len(labyrinth[0])
    visited = set()
    priority_queue = [(heuristic[start], start, [start])]

    iteration = 1

    while priority_queue:
        _, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path, iteration

        if current not in visited:
            visited.add(current)

            i, j = current
            neighbors = []

            # Obtener vecinos válidos
            if i > 0 and labyrinth[i - 1][j] != '0':
                neighbors.append((i - 1, j))
            if i < rows - 1 and labyrinth[i + 1][j] != '0':
                neighbors.append((i + 1, j))
            if j > 0 and labyrinth[i][j - 1] != '0':
                neighbors.append((i, j - 1))
            if j < cols - 1 and labyrinth[i][j + 1] != '0':
                neighbors.append((i, j + 1))

            for neighbor in neighbors:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))

        iteration += 1

    return None, iteration

# Función para cargar el laberinto desde un archivo de texto
def load_labyrinth(file_path):
    with open(file_path, 'r') as file:
        labyrinth = [list(line.strip()) for line in file.readlines()]
    return labyrinth

# Visualización del laberinto y el camino
def visualize_labyrinth(labyrinth, path):
    fig, ax = plt.subplots()

    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[0])):
            cell = labyrinth[i][j]
            color = 'white' if cell == '1' else 'black' if cell == '0' else 'green' if cell == '2' else 'red' if cell == '3' else 'white'
            rect = patches.Rectangle((j, -i), 1, 1, linewidth=1, edgecolor='black', facecolor=color)
            ax.add_patch(rect)

    if path:
        path_x, path_y = zip(*path)
        ax.plot(path_y, [-x for x in path_x], marker='o', color='blue')

    ax.set_xlim(0, len(labyrinth[0]))
    ax.set_ylim(-len(labyrinth), 0)
    ax.set_aspect('equal', adjustable='box')
    plt.show()

# Cargar laberinto desde el archivo
laberinto_path = 'Prueba_3.txt'
laberinto = load_labyrinth(laberinto_path)

# Encontrar la entrada y salida del laberinto
for i in range(len(laberinto)):
    for j in range(len(laberinto[0])):
        if laberinto[i][j] == '2':
            start_node = (i, j)
        elif laberinto[i][j] == '3':
            goal_node = (i, j)

# Ejecutar Greedy Best-First Search
start_time = time.time()
path, iterations = greedy_best_first_search(laberinto, start_node, goal_node, {(i, j): 0 for i in range(len(laberinto)) for j in range(len(laberinto[0]))})
end_time = time.time()

# Imprimir resultados
if path:
    print("El laberinto fue resuelto.")
    print(f"Camino encontrado: {path}")
    print(f"Número total de iteraciones: {iterations}")
    print(f"Tiempo total de ejecución: {end_time - start_time} segundos")
else:
    print("No se encontró un camino válido para resolver el laberinto.")
    print(f"Número total de iteraciones: {iterations}")
    print(f"Tiempo total de ejecución: {end_time - start_time} segundos")

# Visualización del laberinto y el camino
visualize_labyrinth(laberinto, path)

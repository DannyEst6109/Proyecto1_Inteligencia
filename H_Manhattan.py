import time
import heapq
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Función para realizar A* con heurística de Distancia Manhattan
def astar_search_manhattan(labyrinth, start, goal):
    def manhattan_distance(node1, node2):
        return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

    visited = set()
    priority_queue = [(0 + manhattan_distance(start, goal), 0, start, [start])]

    iteration = 1

    while priority_queue:
        _, cost, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path, iteration

        if current not in visited:
            visited.add(current)

            i, j = current
            neighbors = []

            # Obtener vecinos válidos
            if i > 0 and labyrinth[i - 1][j] != '0':
                neighbors.append((i - 1, j))
            if i < len(labyrinth) - 1 and labyrinth[i + 1][j] != '0':
                neighbors.append((i + 1, j))
            if j > 0 and labyrinth[i][j - 1] != '0':
                neighbors.append((i, j - 1))
            if j < len(labyrinth[0]) - 1 and labyrinth[i][j + 1] != '0':
                neighbors.append((i, j + 1))

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_cost = cost + 1  # Costo del movimiento (puede ajustarse según el problema)
                    heapq.heappush(priority_queue, (new_cost + manhattan_distance(neighbor, goal), new_cost, neighbor, path + [neighbor]))

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

# Ejecutar A* con heurística de Distancia Manhattan
start_time = time.time()
path, iterations = astar_search_manhattan(laberinto, start_node, goal_node)
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

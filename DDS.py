import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Función para realizar Depth-Limited Search en el contexto de un laberinto representado como una matriz
def depth_limited_search(labyrinth, start, goal, depth_limit):
    visited = set()
    stack = [(start, [start], 0)]

    iteration = 1

    while stack:
        current, path, depth = stack.pop()

        if current == goal:
            return path, iteration

        if depth < depth_limit and current not in visited:
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
                    stack.append((neighbor, path + [neighbor], depth + 1))

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
            # Cambiar el color según el valor de la celda: 0 es negro (pared), 1 es blanco (camino), 2 es verde (inicio), 3 es rojo (meta)
            color = 'black' if cell == '0' else 'white' if cell == '1' else 'green' if cell == '2' else 'red' if cell == '3' else 'white'
            rect = patches.Rectangle((j, -i), 1, 1, linewidth=1, edgecolor='black', facecolor=color)
            ax.add_patch(rect)

    # Dibujar el camino en azul
    path_x, path_y = zip(*path)
    plt.plot(path_y, [-x for x in path_x], marker='o', color='blue')

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

# Establecer el límite de profundidad para la búsqueda
depth_limit = 400

# Ejecutar Depth-Limited Search
start_time = time.time()
path, iterations = depth_limited_search(laberinto, start_node, goal_node, depth_limit)
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

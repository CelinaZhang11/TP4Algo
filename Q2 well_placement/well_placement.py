# Maltais, 20244617
# Zhang, 20207461

import sys

def read_problem(MyGraph, input_file="input.txt"):
    """Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier,
    faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
    d'autres librairies.
    Functions to read/write in files. you can modify them, do some parsing,
    add a return value, but don't use other librairies"""

    # lecture du fichier/file reading
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()

    firstLine = lines[0].strip()
    parts = firstLine.split()
    height = int(parts[0])
    width = int(parts[1])

    for i in range(1, height + 1):
        gridLine = lines[i].strip()
        gridList = list(gridLine)
        MyGraph.append(gridList)

    return height, width
    
def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()

def dfs(MyGraph, x, y, visited, height, width):
    stack = []
    size = 0   # total count of 1's connected
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    # check initial node
    if not visited[x][y] and MyGraph[x][y] == '1':
        stack.append((x, y))
        visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        size += 1
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < height and 0 <= ny < width and not visited[nx][ny] and MyGraph[nx][ny] == '1':
                stack.append((nx, ny))
                visited[nx][ny] = True
    return size

def main(args):
    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]
    
    # init
    MyGraph = []
    height, width = read_problem(MyGraph, input_file)
    visited = [[False] * width for _ in range(height)]   # no cell has been visited at the start
    sizes = []

    for i in range(height):
        for j in range(width):
            # DFS from cell (i,j) if cell contains 1
            if MyGraph[i][j] == '1' and not visited[i][j]:
                component_size = dfs(MyGraph, i, j, visited, height, width)
                sizes.append(component_size)

    # find the largest connection
    answer = max(sizes) if sizes else 0

    # answering
    write(output_file, str(answer))

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])
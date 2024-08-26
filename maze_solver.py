import os
import time
from queue import Queue

class MAZE_SOLVER():
    def __init__(self, maze, forward_x: int, forward_y: int, i: int, j: int) -> None:
        self.x = i  # Coordenada x del MAZE_SOLVER
        self.y = j  # Coordenada y del MAZE_SOLVER
        self.forward_x = forward_x  # Coordenada x hacia la que está mirando
        self.forward_y = forward_y  # Coordenada y hacia la que está mirando
        self.maze = maze  # Laberinto a resolver
        self.orientation = None  # Orientación del MAZE_SOLVER
        self.def_orientation()  # Definir la orientación del MAZE_SOLVER
        self.rows = len(maze)
        self.cols = len(maze[0]) if self.rows > 0 else 0
        self.visited = set()  # Conjunto para guardar posiciones visitadas
        self.queue = Queue()  # Cola para BFS

    def show(self) -> None:
        """Método para imprimir el laberinto y la información del MAZE_SOLVER"""
        for i in range(self.rows):
            for j in range(self.cols):
                if i == self.x and j == self.y:
                    print('\t[X]', end='')
                else:
                    print(f'\t{self.maze[i][j]}', end='')
            print('\n')
        print(f'\t\t\t    Posición actual: ( {self.x}, {self.y} )')
        print(f'\t\t\t\tMirando a: ( {self.forward_x}, {self.forward_y} )')
        print()

    def exists(self, x: int, y: int) -> bool:
        """Método para verificar si las coordenadas existen en el laberinto"""
        return 0 <= x < self.rows and 0 <= y < self.cols

    def def_orientation(self):
        """Definir la orientación del MAZE_SOLVER"""
        if self.forward_x > self.x and self.forward_y == self.y:
            self.orientation = 'S'
        elif self.forward_x == self.x and self.forward_y < self.y:
            self.orientation = 'W'
        elif self.forward_x < self.x and self.forward_y == self.y:
            self.orientation = 'N'
        elif self.forward_x == self.x and self.forward_y > self.y:
            self.orientation = 'E'

    def solve_bfs(self) -> None:
        """Resolver el laberinto utilizando BFS"""
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Movimientos posibles (S, N, E, W)
        self.queue.put((self.x, self.y))  # Inicializar la cola con la posición de inicio
        self.visited.add((self.x, self.y))

        while not self.queue.empty():
            x, y = self.queue.get()
            self.x, self.y = x, y  # Actualizar posición actual
            self.show()
            #time.sleep(0.4)
            #os.system('cls')

            # Verificar si hemos llegado a la meta
            if self.maze[x][y] == 'M':
                print("\n\n\t\t==-==-==-==-==-== M E T A ==-==-==-==-==-==")
                self.show()
                print('¡LLEGASTE A LA META!')
                return

            # Explorar vecinos en direcciones horizontales y verticales
            for direction in directions:
                new_x, new_y = x + direction[0], y + direction[1]
                
                if self.exists(new_x, new_y) and (new_x, new_y) not in self.visited:
                    if self.maze[new_x][new_y] == 0 or self.maze[new_x][new_y] == 'M':
                        self.queue.put((new_x, new_y))
                        self.visited.add((new_x, new_y))

        print("¡No se encontró la meta!")

def find_start(maze):
    """Encuentra las coordenadas de inicio 'S' en el laberinto."""
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                return (i, j)
    return None

ex1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 0, 0, 1, 1, 0, 0],
       [0, 1, 0, 'M', 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       ['S', 1, 0, 0, 0, 0, 1, 0, 0],
       [0, 1, 1, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]

if __name__ == "__main__":
    os.system('cls')
    [i, j] = find_start(ex1)
    mz = MAZE_SOLVER(ex1, i+1, j, i, j)
    mz.solve_bfs()

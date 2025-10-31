import sys
from collections import deque


def read_maze(filename: str) -> list[list[str]]:

    try:
        with open(filename, "r") as file:
            list_of_maze = file.read().splitlines()
            return list_of_maze
    except FileNotFoundError:
        sys.exit("File not found.")


def find_start_and_target(maze: list[list[str]]) -> tuple[int, int]:

    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == "S":
               s_position = (row, column)
            if maze[row][column] == "T":
                t_position = (row, column)
    return s_position, t_position


def get_neighbors(maze: list[list[str]], position: tuple[int, int]) -> list[tuple[int, int]]:

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbors = []

    for direction in directions:
        row, column = position[0] + direction[0], position[1] + direction[1]
        if 0 <= row < len(maze) and 0 <= column < len(maze[0]):
            if maze[row][column] != "#":
                neighbors.append((row, column))

    return neighbors


def bfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]] | None:

    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        position, path = queue.popleft()
        if position == target:
            return path

        for neighbor in get_neighbors(maze, position):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


def dfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:

    visited = {start}
    stack = [(start, [start])]

    while stack:
        position, path = stack.pop()

        for neighbor in get_neighbors(maze, position):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
        if position == target:
            return path


def print_maze_with_path(maze: list[list[str]], path: list[tuple[int, int]]) -> None:

    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    maze_copy = [list(row) for row in maze]

    for r, c in path:
        if maze_copy[r][c] == 'S':
            maze_copy[r][c] = f'{YELLOW}S{RESET}'
        elif maze_copy[r][c] == 'T':
            maze_copy[r][c] = f'{GREEN}T{RESET}'
        elif maze_copy[r][c] not in ('S', 'T'):
            maze_copy[r][c] = f'{RED}x{RESET}'
    for row in maze_copy:
        print("".join(row))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python ex05.py <algorithm> <filename>")

    alg = sys.argv[1]
    filename = sys.argv[2]

    list_maze = read_maze(filename)
    start = find_start_and_target(list_maze)[0]
    target = find_start_and_target(list_maze)[1]

    if alg == "bfs":
        print_maze_with_path(list_maze, bfs(list_maze, start, target))
    elif alg == "dfs":
        print_maze_with_path(list_maze, dfs(list_maze, start, target))

def load_maze(filename="maze.txt"):
    with open(filename) as maze_file:
        maze_text = maze_file.read()

    # Transform text file to the matrix of maze
    maze_lines = maze_text.splitlines()
    maze = [list(line) for line in maze_lines]
    
    start = find_symbol_in_maze('0', maze)        
    finish = find_symbol_in_maze('F', maze)
    
    return maze, start, finish


def find_symbol_in_maze(symbol, maze):
    for row_i, row in enumerate(maze):
        try:
            x = row.index(symbol)
        except ValueError:
            continue
        y = row_i
        return (x, y)
    
    raise ValueError(f"{symbol} not found in Maze")
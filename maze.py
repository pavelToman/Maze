with open("maze.txt") as maze_file:
    maze_text = maze_file.read()

# Transform text file to the matrix of maze
maze_lines = maze_text.splitlines()
maze = list()
for line in maze_lines:
    maze.append(list(line))

# Find coordinates (x,y) of start "0"
for row in maze:
    if "0" in row:
        y = maze.index(row)
        x = row.index("0")
start = (x, y)

# Find coordinates (x,y) of finish "F"
for row in maze:
    if "F" in row:
        y = maze.index(row)
        x = row.index("F")
finish = (x, y)

# Queue of coordinates (x,y) of the road " " (space)
queue = list()
queue.append(list())
queue[0].append(start)

# Queue has levels
# coordinates of the start are at queue_level=0
queue_level = 0
level = queue_level

# Shortest path across the maze
shortest_path = list()

# Checking functions
# is it possible to go up/down/right/left and is it the finish?
search_for_path = True
road = " "

while search_for_path:
    queue.append(list())  # creat next level of queue
    for coordinates in queue[level]:
        x, y = coordinates

        # UP check
        up = maze[y-1][x]
        up_coordinates = (x, y - 1)
        up_y_coordinate = y - 1
        if up_coordinates == finish:
            shortest_path.append(coordinates)
            queue.pop()
            search_for_path = False
        elif up_y_coordinate >= 0:
            if up == road:
                next_level = level + 1
                queue[next_level].append(up_coordinates)
                maze[y-1][x] = next_level

        # DOWN chceck
        down = maze[y+1][x]
        down_coordinates = (x, y + 1)
        down_y_coordinates = y + 1
        if down_coordinates == finish:
            shortest_path.append(coordinates)
            queue.pop()
            search_for_path = False
        elif down_y_coordinates <= len(maze):
            if down == road:
                next_level = level + 1
                queue[next_level].append(down_coordinates)
                maze[y+1][x] = next_level

        # LEFT check
        left = maze[y][x-1]
        left_coordinates = (x - 1, y)
        left_x_coordinates = x - 1
        if left_coordinates == finish:
            shortest_path.append(coordinates)
            queue.pop()
            search_for_path = False
        elif left_x_coordinates >= 0:
            if left == road:
                next_level = level + 1
                queue[next_level].append(left_coordinates)
                maze[y][x-1] = next_level

        # RIGHT check
        right = maze[y][x+1]
        right_coordinates = (x + 1, y)
        right_x_coordiantes = x + 1
        if right_coordinates == finish:
            shortest_path.append(coordinates)
            queue.pop()
            search_for_path = False
        elif right_x_coordiantes <= len(maze[y]):
            if right == road:
                next_level = level + 1
                queue[next_level].append(right_coordinates)
                maze[y][x+1] = next_level

    # If there is no way to move - can't go trough the maze
    if not queue[-1]:
        print("There is no way from start do finish in this maze!")
        search_for_path = False
    # If I found field next to the finish
    # I can creat the shortest path
    elif len(shortest_path) != 0:
        for i in range(level):
            x, y = shortest_path[-1]
            previous_level = level - 1
            up = maze[y-1][x]
            up_coordinates = (x, y - 1)
            down = maze[y+1][x]
            down_coordinates = (x, y + 1)
            left = maze[y][x-1]
            left_coordinates = (x - 1, y)
            right = maze[y][x+1]
            right_coordinates = (x + 1, y)
            if up == previous_level:
                shortest_path.append(up_coordinates)
            elif down == previous_level:
                shortest_path.append(down_coordinates)
            elif left == previous_level:
                shortest_path.append(left_coordinates)
            elif right == previous_level:
                shortest_path.append(right_coordinates)
            level -= 1
        # Print maze with shortest path as path of "#"
        maze = list()
        for lines in maze_lines:
            maze.append(list(lines))
        for coordinates in shortest_path:
            x, y = coordinates
            maze[y][x] = "#"
        for line in maze:
            line = " ".join(line)
            print(line)
    # If I didn't find field next to the finish, search continue
    else:
        level += 1
        continue

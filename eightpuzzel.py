import numpy as np

# Function to generate child states of the puzzle


def generate_child(puzzle, level, direction):
    empty_cell = np.argwhere(puzzle == '_')[0]
    moves = [(0, -1, 'left'), (0, 1, 'right'), (-1, 0, 'up'), (1, 0, 'down')]
    children = []

    for move in moves:
        new_position = empty_cell + move[:2]
        if (0 <= new_position[0] < puzzle.shape[0] and 0 <= new_position[1] < puzzle.shape[1]):
            child = np.copy(puzzle)
            child[empty_cell[0], empty_cell[1]] = puzzle[new_position[0], new_position[1]]
            child[new_position[0], new_position[1]] = '_'
            children.append((child, level + 1, move[2]))  # Include direction

    return children

# Function to calculate the heuristic values (h and f) for a state


def calculate_f_h(start, goal, level):
    h_value = np.sum(start != goal)
    return h_value, h_value + level

# Function to print the current state of the puzzle


def print_puzzle(puzzle, direction):
    for row in puzzle:
        print(*row)
    print("Empty cell moved:", direction, '\n')

# The A* search algorithm


def a_star(start, goal):
    open_list = [(start, 0, '')]
    closed_list = set()
    level = 0
    while open_list:
        open_list.sort(key=lambda x: calculate_f_h(x[0], goal, level)[1])
        cur, level, direction = open_list.pop(0)
        closed_list.add(tuple(map(tuple, cur)))

        h_value, f_value = calculate_f_h(cur, goal, level)

        if level != 0:
            print_puzzle(cur, direction)
        if h_value == 0:
            print("Goal reached!")
            break

        print("Step:", level + 1)
        best_child = None
        best_h_value = float('inf')
        for child, child_level, child_direction in generate_child(cur, level, direction):
            if tuple(map(tuple, child)) not in closed_list:
                h_value, _ = calculate_f_h(child, goal, level)
                if h_value < best_h_value:
                    best_child = child
                    best_h_value = h_value
                    best_direction = child_direction

        if best_child is not None:
            open_list.append((best_child, level + 1, best_direction))

# Function to accept input for the puzzle states


def accept():
    puz = []
    for i in range(3):
        temp = list(input().split(" "))
        puz.append(temp)
    return np.array(puz)


# Main program
print("Enter the start state matrix")
start = accept()
print("Enter the goal state matrix")
goal = accept()
a_star(start, goal)

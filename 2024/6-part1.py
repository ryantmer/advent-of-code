from enum import Enum
from functools import reduce
import sys

# is this <software developemente>?
print(sys.setrecursionlimit(20000))

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def turn_right(self):
        return Direction((self.value + 1) % len(Direction))

input_data = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]
input_data = open("6-input.txt", "r")

input = [str(line).strip() for line in input_data]

max_row = len(input)
max_col = len(input[0])

current_row = [index for index, row in enumerate(input) if "^" in row][0]
current_col = [index for index, val in enumerate(input[current_row]) if val == "^"][0]
print("Starting at row = %d, col = %d" % (current_row, current_col))

def move(row, col, dir):
    input[row] = input[row][:col] + 'X' + input[row][col + 1:]
    # print('------------------------------')
    # print('Current state:')
    # print('\n'.join(input))
    # print("--> Attempting to move %s from %d,%d" % (dir, row, col))
    row_increment = col_increment = 0

    if dir == Direction.NORTH:
        row_increment = -1
    elif dir == Direction.SOUTH:
        row_increment = 1
    elif dir == Direction.EAST:
        col_increment = 1
    elif dir == Direction.WEST:
        col_increment = -1

    next_row = row + row_increment
    next_col = col + col_increment
    if next_row < 0 or next_col < 0 or next_row >= max_row or next_col >= max_col:
        # print("Moving %s from %d %d moves off the board" % (dir, row, col))
        return

    while input[next_row][next_col] == '#':
        # print("Moving %s from %d %d is not possible, need to turn right" % (dir, row, col))
        if dir == Direction.NORTH:
            next_row = row
            next_col = col + 1
        elif dir == Direction.SOUTH:
            next_row = row
            next_col = col - 1
        elif dir == Direction.EAST:
            next_row = row + 1
            next_col = col
        elif dir == Direction.WEST:
            next_row = row - 1
            next_col = col
        dir = dir.turn_right()
        print("--> Rotated, and now moving %s to %d %d" % (dir, next_row, next_col))

    try:
        move(next_row, next_col, dir)
    except RecursionError:
        return

move(current_row, current_col, dir=Direction.NORTH)

sum = reduce(lambda x, y: x + y, [reduce(lambda x, y: x + y, [1 if val == 'X' else 0 for val in row]) for row in input])

print("Part 1: The guard visits %d distinct positions" % sum)

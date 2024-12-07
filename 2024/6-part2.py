from enum import Enum
from functools import reduce
import sys

# is this <software developemente>?
sys.setrecursionlimit(20000)

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

start_row = [index for index, row in enumerate(input) if "^" in row][0]
start_col = [index for index, val in enumerate(input[start_row]) if val == "^"][0]
print("Starting at row = %d, col = %d" % (start_row, start_col))

loop_count = 0

def move(map_layout, row, col, dir):
    global loop_count

    map_layout[row] = map_layout[row][:col] + "X" + map_layout[row][col + 1:]
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
        return

    while map_layout[next_row][next_col] == "#" or map_layout[next_row][next_col] == "$":
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

    try:
        move(map_layout, next_row, next_col, dir)
    except RecursionError:
        map_layout[row] = map_layout[row][:col] + "!" + map_layout[row][col + 1:]
        loop_count += 1
        return

for row, _ in enumerate(input):
    print("Iterating through row %d" % row)
    for col, _ in enumerate(input[row]):
        map_layout = [row[:] for row in input]
        map_layout[row] = map_layout[row][:col] + "$" + map_layout[row][col + 1:]

        # print("Looking for loops in layout:")
        # print("\n".join(map_layout))

        move(map_layout, start_row, start_col, Direction.NORTH)

print("Part 2: %d loops found" % loop_count)

input_data = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]
input_data = open("4-input.txt", "r")

matrix = [[x for x in line] for line in input_data]
x_max = len(matrix[0])
y_max = len(matrix)

def is_x_mas(y, x):
    centre = matrix[y][x]
    if centre != 'A':
        return False
    
    if x - 1 < 0 or y - 1 < 0 or x + 1 >= x_max or y + 1 >= y_max:
        return False
    
    top_left = matrix[y-1][x-1]
    top_right = matrix[y-1][x+1]
    bottom_left = matrix[y+1][x-1]
    bottom_right = matrix[y+1][x+1]
    return (top_left == 'M' and bottom_right == 'S' or top_left == 'S' and bottom_right == 'M') and \
        (top_right == 'M' and bottom_left == 'S' or top_right == 'S' and bottom_left == 'M')

x_mas_count = 0
for y in range(y_max):
    for x in range(x_max):
        if is_x_mas(y, x):
            # print("--> Found at %d %d" % (y + 1, x + 1))
            x_mas_count += 1

print("Part 2: %d X-MASes found" % x_mas_count)
    
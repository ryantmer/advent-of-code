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

def part1():
    def is_xmas(x, y, x_increment, y_increment):
        if x_increment == 0 and y_increment == 0:
            return False
        if x + x_increment * 3 < 0 or x + x_increment * 3 > x_max or y + y_increment * 3 < 0 or y + y_increment * 3 > y_max:
            return False

        try:
            # print("x=%d y=%d %d %d" % (x, y, x_increment, y_increment), "Checking " + matrix[y][x] + matrix[y + y_increment][x + x_increment] + matrix[y + y_increment * 2][x + x_increment * 2] + matrix[y + y_increment * 3][x + x_increment * 3])
            return matrix[y][x] + matrix[y + y_increment][x + x_increment] + matrix[y + y_increment * 2][x + x_increment * 2] + matrix[y + y_increment * 3][x + x_increment * 3] == 'XMAS'
        except IndexError:
            return False

    def count_xmas(x, y):
        count = 0
        for x_increment in range(-1, 2, 1):
            for y_increment in range(-1, 2, 1):
                if is_xmas(x, y, x_increment, y_increment):
                    # print("--> Found at %d %d with %d %d" % (x + 1, y + 1, x_increment, y_increment))
                    count += 1
                
        return count

    xmas_count = 0
    for x in range(x_max):
        for y in range(y_max):
            xmas_count += count_xmas(x, y)
    print("Part 1: %d XMASes found" % xmas_count)

def part2():
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

part1()
part2()

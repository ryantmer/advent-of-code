input = [
    "0123",
    "1234",
    "8765",
    "9876",
]
input = [
    "89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732",
]
file_input = open("10-input.txt", "r")
input = [line.strip() for line in file_input]

trail_start = 0
trail_end = 9
max_row = len(input) - 1
max_col = len(input[0]) - 1

trailheads = list()
for row_index, row in enumerate(input):
    trailheads += [(row_index, col_index) for col_index, val in enumerate(row) if val == str(trail_start)]
print("There are %d trailheads" % len(trailheads))

def out_of_bounds(row, col):
    return row < 0 or row > max_row or col < 0 or col > max_col

def part1():
    def get_reachable_trail_ends(reachable_trail_ends, prev_values, row, col):
        prev_value = prev_values[-1]
        if prev_value == trail_end:
            reachable_trail_ends.add((row, col))

        for row_increment, col_increment in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            next_row = row + row_increment
            next_col = col + col_increment
            if out_of_bounds(next_row, next_col):
                continue

            next_value = int(input[next_row][next_col])
            if prev_value + 1 != next_value:
                # Not a 1-increment, skip this direction
                continue

            trail_so_far = prev_values[:] + [next_value]
            get_reachable_trail_ends(reachable_trail_ends, trail_so_far, next_row, next_col)

        return reachable_trail_ends

    trailhead_score_sum = 0
    for trailhead in trailheads:
        # print("Checking trailhead", trailhead)
        result = get_reachable_trail_ends(set(), [0], trailhead[0], trailhead[1])
        trailhead_score = len(result)
        # print("Result:", result, "Trailhead score:", trailhead_score)
        trailhead_score_sum += trailhead_score

    print("Part 1: Total trailhead score is %d" % trailhead_score_sum)

def part2():
    def get_next_step(prev_values, row, col):
        prev_value = prev_values[-1]
        if prev_value == trail_end:
            return [prev_values]

        paths = []
        for row_increment, col_increment in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            next_row = row + row_increment
            next_col = col + col_increment
            if out_of_bounds(next_row, next_col):
                continue

            next_value = int(input[row + row_increment][col + col_increment])
            if prev_value + 1 != next_value:
                # Not a 1-increment, skip this direction
                continue

            trail_so_far = prev_values[:] + [next_value]
            result = get_next_step(trail_so_far, row + row_increment, col + col_increment)
            if len(result) > 0:
                paths.extend([x for x in result])
        
        return paths

    trailhead_score_sum = 0
    for trailhead in trailheads:
        # print("Checking trailhead", trailhead)
        result = get_next_step([0], trailhead[0], trailhead[1])
        trailhead_score = len(result)
        # print("Result:", result, "Trailhead score:", trailhead_score)
        trailhead_score_sum += trailhead_score

    print("Part 2: Total trailhead score is %d" % trailhead_score_sum)

part1()
part2()

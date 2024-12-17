input = [
    "AAAA",
    "BBCD",
    "BBCC",
    "EEEC",
]
input = [
    "EEEEE",
    "EXXXX",
    "EEEEE",
    "EXXXX",
    "EEEEE",
]
# input = [
#     "AAAAAA",
#     "AAABBA",
#     "AAABBA",
#     "ABBAAA",
#     "ABBAAA",
#     "AAAAAA",
# ]
# input = [
#     "RRRRIICCFF",
#     "RRRRIICCCF",
#     "VVRRRCCFFF",
#     "VVRCCCJFFF",
#     "VVVVCJJCFE",
#     "VVIVCCJJEE",
#     "VVIIICJJEE",
#     "MIIIIIJJEE",
#     "MIIISIJEEE",
#     "MMMISSJEEE",
# ]
# file_input = open("12-input.txt", "r")
# input = [line.strip() for line in file_input]

max_row: int = len(input) - 1
max_col: int = len(input[0]) - 1

class Direction:
    Name = ""
    def __init__(self, row: int, col: int):
        self.RowOffset = row
        self.ColOffset = col
        if row == 0:
            self.Name = "Right" if col == 1 else "Left"
        else:
            self.Name = "Down" if row == 1 else "Up"
    def __str__(self):
        return self.Name
    def __eq__(self, other):
        if isinstance(other, Direction):
            return self.RowOffset == other.RowOffset and self.ColOffset == other.ColOffset
        return False
    def __hash__(self):
        return id(self)

Left = Direction(0, -1)
Up = Direction(-1, 0)
Down = Direction(1, 0)
Right = Direction(0, 1)
directions = [Left, Up, Down, Right]

def out_of_bounds(row: int, col: int):
    return row < 0 or row > max_row or col < 0 or col > max_col

def part1():
    # Anything that has already been analysed as part of another region with the same plant type
    processed_plots: set[tuple[int, int]] = set()

    def calculate_region_stats(recursion_depth: int, plant_type: str, row: int, col: int):
        # print("-" * recursion_depth, "Calculating cost", row, col, plant_type)
        processed_plots.add((row, col))
        perimeter = 0
        area = 1
        for direction in directions:
            next_row = row + direction.RowOffset
            next_col = col + direction.ColOffset
            if out_of_bounds(next_row, next_col):
                # If this direction is the edge, fence it off
                perimeter += 1
            elif input[next_row][next_col] != plant_type:
                # This direction hits a different plant type, fence off that direction
                perimeter += 1
            elif (next_row, next_col) in processed_plots:
                # We're looping back to a plot that's already been processed, skip it
                continue
            else:
                # This direction is a continuation of this plot
                (add_perimeter, add_area) = calculate_region_stats(recursion_depth + 1, plant_type, next_row, next_col)
                perimeter += add_perimeter
                area += add_area

        # print("-" * recursion_depth, "Perimeter", row, col, perimeter)
        return (perimeter, area)

    total_cost = 0
    for row_index, row in enumerate(input):
        for col_index, plant_type in enumerate(row):
            if (row_index, col_index) in processed_plots:
                # This plot has already been processed as part of another region
                continue

            (region_perimeter, region_area) = calculate_region_stats(0, plant_type, row_index, col_index)
            print("Region perimeter for %s starting at %d %d is %d; area is %d" % (plant_type, row_index, col_index, region_perimeter, region_area))
            total_cost += region_area * region_perimeter
    print("Part 1: total cost is", total_cost)

def part2():
    # Anything that has alraedy been analysed as part of another region with the same plant type
    processed_plots: set[tuple[int, int]] = set()
    
    def calculate_region_stats(existing_fences: dict[Direction, set[int, int]], plant_type: str, row: int, col: int):
        processed_plots.add((row, col))
        sides = 0
        area = 1

        for direction in directions:
            next_row = row + direction.RowOffset
            next_col = col + direction.ColOffset
            add_sides = 0
            if out_of_bounds(next_row, next_col) or input[next_row][next_col] != plant_type:
                # Next step is out of bounds or a different plant type, add a fence in that direction
                if direction not in existing_fences:
                    existing_fences[direction] = set()
                
                # If no adjacent plots have a fence on the same side, add a side
                if (row, col + 1) not in existing_fences[direction] and \
                    (row, col - 1) not in existing_fences[direction] and \
                    (row + 1, col) not in existing_fences[direction] and \
                    (row - 1, col) not in existing_fences[direction]:
                    add_sides += 1
                
                existing_fences[direction].add((row, col))
            elif (next_row, next_col) in processed_plots:
                # We're looping back to a plot that's already been processed, skip it
                pass
            else:
                # This direction is a continuation of this plot
                (recursive_add_sides, add_area) = calculate_region_stats(existing_fences, plant_type, next_row, next_col)
                add_sides += recursive_add_sides
                area += add_area
            sides += add_sides

        return (sides, area)

    total_cost = 0
    for row_index, row in enumerate(input):
        for col_index, plant_type in enumerate(row):
            if (row_index, col_index) in processed_plots:
                # This plot has already been processed as part of another region
                continue

            all_fences = dict()
            (region_sides, region_area) = calculate_region_stats(all_fences, plant_type, row_index, col_index)
            print("************ Region sides for %s starting at %d %d is %d; area is %d" % (plant_type, row_index, col_index, region_sides, region_area))
            total_cost += region_area * region_sides
            if plant_type == "A":
                print([(str(direction), [fence for fence in sorted(all_fences[direction])]) for direction in all_fences])
    print("Part 2: total cost is", total_cost)

# part1()
part2()

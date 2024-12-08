input_data = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............",
]
input_data = open("8-input.txt", "r")
input = [line.strip() for line in input_data]

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.row == other.row and self.col == other.col
        return False

    def __hash__(self):
        return hash((self.row, self.col))

    def is_within_range(self):
        return self.row >= 0 and self.col >= 0 and self.row < len(input) and self.col < len(input[0])

def get_antinodes(frequency, nodes_by_frequency, include_resonant=False):
    # print("Checking frequency", frequency, "for antinodes")
    antinodes = set()
    for node in nodes_by_frequency[frequency]:
        for other_node in nodes_by_frequency[frequency]:
            if node == other_node:
                continue

            row_diff = node.row - other_node.row
            col_diff = node.col - other_node.col
            if include_resonant:
                antinodes.add(node)
                # Include all resonant antinodes (part 2)
                antinode = Node(node.row + row_diff, node.col + col_diff)
                while antinode.is_within_range():
                    antinodes.add(antinode)
                    antinode = Node(antinode.row + row_diff, antinode.col + col_diff)
            else:
                # Just find the first antinode (part 1)
                antinode = Node(node.row + row_diff, node.col + col_diff)
                if antinode.is_within_range():
                    antinodes.add(antinode)

    return antinodes

def print_antinode_map(antinodes, input):
    antinode_map = input[:]
    for antinode in antinodes:
        antinode_map[antinode.row] = antinode_map[antinode.row][:antinode.col] + '#' + antinode_map[antinode.row][antinode.col + 1:]
    print('\n'.join(antinode_map))

# Map locations of all nodes for each frequency
nodes_by_frequency = dict()
for row_index, row in enumerate(input):
    for col_index, val in enumerate(row):
        if val == '.':
            continue

        if val not in nodes_by_frequency:
            nodes_by_frequency[val] = []
        
        # print("Adding frequency %s to dict" % val)
        nodes_by_frequency[val].append(Node(row_index, col_index))

antinodes = set()
resonant_antinodes = set()
for frequency in nodes_by_frequency:
    antinodes |= get_antinodes(frequency, nodes_by_frequency)
    resonant_antinodes |= get_antinodes(frequency, nodes_by_frequency, include_resonant=True)

# print_antinode_map(antinodes, input)
# print("Antinodes", sorted([(node.row, node.col) for node in antinodes]))
print("Part 1: There are %d antinodes" % len(antinodes))

# print_antinode_map(resonant_antinodes, input)
# print("Resonant antinodes", sorted([(node.row, node.col) for node in resonant_antinodes]))
print("Part 2: There are %d resonant antinodes" % len(resonant_antinodes))

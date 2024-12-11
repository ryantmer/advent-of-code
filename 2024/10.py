input_data = [
    "89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732",
]

trailheads = list()
for row_index, row in enumerate(input_data):
	trailheads += [(row_index, col_index) for col_index, val in enumerate(row) if val == '0']
print("There are %d trailheads" % len(trailheads))

def find_next_valid_steps(row, col):
	pass

for trailhead in trailheads:
	pass

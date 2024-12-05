input_data = [
	"3   4",
	"4   3",
	"2   5",
	"1   3",
	"3   9",
	"3   3",
]
input_data = open("1-input.txt", "r")

input = [[int(x) for x in line.split("   ")] for line in input_data]

# Rotate to be two n-length lists
[left_list, right_list] = [sorted(list(x)) for x in list(zip(*input[::-1]))]
# Find the absolute different between each (now sorted) pair
diff = [abs(c - a) for c, a in zip(left_list, right_list)]
# Answer is the sum of the absolute differences
print("Part 1 answer:", sum(diff))

# Calculate the number of times each left value occurs in the right list
similarity_score = sum([right_list.count(x) * x for x in left_list])
print("Part 2 answer", similarity_score)

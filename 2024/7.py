input_data = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20",
]
input_data = open("7-input.txt", "r")

def build_result_tree(line, include_concatenation_operator=False):
    test_value, first_factor, *remaining_factors = map(int, line.replace(":", "").split())

    operation_results = [first_factor]
    for next_factor in remaining_factors:
        # print(operation_results, next_factor)
        operation_results = [operator(prior_result, next_factor) for prior_result in operation_results for operator in (
            lambda a, b: a + b,
            lambda a, b: a * b,
            lambda a, b: int("%d%d" % (a, b)) if include_concatenation_operator else 0
        )]
        # print("Results tree for %d" % next_factor)
        # print("-->", operation_results)

    if test_value in operation_results:
        return test_value
    else:
        return 0

test_value_sum_part1 = 0
test_value_sum_part2 = 0

for line in input_data:
    test_value_sum_part1 += build_result_tree(line)
    test_value_sum_part2 += build_result_tree(line, True)

print("Part 1: Sum of valid test values is %d" % test_value_sum_part1)
print("Part 2: Sum of valid test values is %d" % test_value_sum_part2)

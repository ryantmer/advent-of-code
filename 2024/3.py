import re
import functools

input_data = [
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
]
input_data = open("3-input.txt", "r")

# Part 1
total_sum = 0
for line in input_data:
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
    tokens = [re.split('\(|,|\)', x) for x in matches]
    multiples = [int(x[1]) * int(x[2]) for x in tokens]
    sum = functools.reduce(lambda x, y: x + y, multiples)
    total_sum += sum

print("Part 1: total sum is %d" % total_sum)

# Part 2
input_data = [
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
]
input_data = open("3-input.txt", "r")

do_mul = True
total_sum = 0
for line in input_data:
    matches = re.findall("(mul\(\d{1,3},\d{1,3}\))|(don't\(\))|(do\(\))", line)
    for match in matches:
        mul, dont, do = match
        if do_mul and mul:
            tokens = re.split('\(|,|\)', mul)
            total_sum += int(tokens[1]) * int(tokens[2])
        elif dont:
            do_mul = False
        elif do:
            do_mul = True

print("Part 2: total sum is %d" % total_sum)

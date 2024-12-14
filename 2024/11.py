import math
from functools import lru_cache

input = "0 1 10 99 999"
input = "125 17"
input = "5688 62084 2 3248809 179 79 0 172169"

blinks = 75
stones = [int(x) for x in input.split(" ")]

def part1():
    result = stones[:]
    for i in range(blinks):
        blink_result = []
        for stone in result:
            if stone == 0:
                blink_result.append(1)
                continue
            
            digits = 1 if stone == 0 else int(math.log10(stone)) + 1
            if digits % 2 == 0:
                lhs = int(stone / (10 ** (digits / 2)))
                rhs = int(stone - lhs * 10 ** (digits / 2))
                blink_result.extend([lhs, rhs])
                continue
            
            blink_result.append(stone * 2024)

        print("After %d blinks, there are %d stones" % (i + 1, len(result)))
        result = blink_result

    print("Part 1: After %d blinks, there are %d stones" % (blinks, len(result)))

# Part 2: Resolve each stone individually
def part2():
    @lru_cache(maxsize=None)
    def process_stone(stone, recursion_depth):
        if recursion_depth == blinks:
            return 1

        if stone == 0:
            return process_stone(1, recursion_depth + 1)

        digits = 1 if stone == 0 else int(math.log10(stone)) + 1
        if digits % 2 == 0:
            lhs = int(stone / (10 ** (digits / 2)))
            rhs = int(stone - lhs * 10 ** (digits / 2))
            return process_stone(lhs, recursion_depth + 1) + process_stone(rhs, recursion_depth + 1)
        
        return process_stone(stone * 2024, recursion_depth + 1)

    result = 0
    for stone in stones:
        final_stone_count = process_stone(stone, 0)
        print("Initial stone %d turns into %d stones" % (stone, final_stone_count))
        result += final_stone_count

    print("Part 2: After %d blinks, there are %d stones" % (blinks, result))

# part1()
part2()

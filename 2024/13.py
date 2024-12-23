import re
import math

input = [
    "Button A: X+94, Y+34",
    "Button B: X+22, Y+67",
    "Prize: X=8400, Y=5400",
    "",
    # "Button A: X+26, Y+66",
    # "Button B: X+67, Y+21",
    # "Prize: X=12748, Y=12176",
    # "",
    # "Button A: X+17, Y+86",
    # "Button B: X+84, Y+37",
    # "Prize: X=7870, Y=6450",
    # "",
    # "Button A: X+69, Y+23",
    # "Button B: X+27, Y+71",
    # "Prize: X=18641, Y=10279",
    # "",
    # "Button A: X+10, Y+20",
    # "Button B: X+20, Y+40",
    # "Prize: X=40, Y=80",
    # "",
    # "Button A: X+100, Y+200",
    # "Button B: X+20, Y+40",
    # "Prize: X=400, Y=800",
    # "",
    # "Button A: X+94, Y+34",
    # "Button B: X+22, Y+67",
    # "Prize: X=12658, Y=3988",
    # "",
    # "Button A: X+13, Y+7",
    # "Button B: X+26, Y+14",
    # "Prize: X=39, Y=21",
    # "",
]
# file_input = open("13-input.txt", "r")
# input = [line.strip() for line in file_input]

a_button_cost = 3
b_button_cost = 1

class XYPoint:
    def __init__(self, x, y):
        self.X = int(x)
        self.Y = int(y)
    def __str__(self):
        return 'X: %d, Y: %d' % (self.X, self.Y)
    def __eq__(self, other):
        if isinstance(other, XYPoint):
            return self.X == other.X and self.Y == other.Y
        return False

button_a_params: list[XYPoint] = [XYPoint(*re.findall(r'\d+', line)) for line_index, line in enumerate(input) if line_index % 4 == 0]
button_b_params: list[XYPoint] = [XYPoint(*re.findall(r'\d+', line)) for line_index, line in enumerate(input) if line_index % 4 == 1]
prize_params: list[XYPoint] = [XYPoint(*re.findall(r'\d+', line)) for line_index, line in enumerate(input) if line_index % 4 == 2]

print([str(x) for x in button_a_params])
print([str(x) for x in button_b_params])
print([str(x) for x in prize_params])

def get_cost(a_presses, b_presses):
    return a_presses * a_button_cost + b_presses * b_button_cost

def get_button_presses(a, b, prize_location):
    candidates = []
    max_b_presses = int(prize_location.X / b.X)
    print('Pressing B %d times gets close, to %d out of %d' % (max_b_presses, max_b_presses * b.X, prize_location.X))
    current = XYPoint(b.X * max_b_presses, b.Y * max_b_presses)
    if current == prize_location:
        candidates.append((0, max_b_presses))
    
    b_presses = max_b_presses
    a_presses = 0
    while b_presses >= 0:
        print('Current location', current, 'with B pressed', b_presses)
        current.X = b_presses * b.X
        current.Y = b_presses * b.Y

        delta_x = prize_location.X - current.X
        delta_y = prize_location.Y - current.Y

        # Now, figure out how many times we can press A to fill in the delta
        potential_a_presses_x = math.floor(delta_x / a.X)
        potential_a_presses_y = math.floor(delta_y / a.Y)

        # And then add that many A presses
        if potential_a_presses_x > 0 and potential_a_presses_y > 0:
            # print('--> With a delta of %d, could press A %d times' % (delta_x, potential_a_presses_x))
            current.X = current.X + (potential_a_presses_x * a.X)
            current.Y = current.Y + (potential_a_presses_x * a.Y)
        
        if current == prize_location:
            a_presses = potential_a_presses_x
            candidates.append((a_presses, b_presses))
            print(a_presses, b_presses, 'is a valid candidate with cost', get_cost(a_presses, b_presses))

        b_presses -= 1
    
    if len(candidates) == 0:
        return (None, None)
    
    min_cost = get_cost(*candidates[0])
    min_cost_candidate = candidates[0]
    for candidate in candidates:
        if get_cost(*candidate) < min_cost:
            min_cost_candidate = candidate

    return min_cost_candidate

token_cost = 0
for machine_number, a in enumerate(button_a_params):
    b = button_b_params[machine_number]
    prize_location = prize_params[machine_number]
    (a_presses, b_presses) = get_button_presses(a, b, prize_location)
    if a_presses is not None:
        print('Machine #%d can be won with A*%d, B*%d, costing %d' % (machine_number, a_presses, b_presses, a_presses * a_button_cost + b_presses * b_button_cost))
        token_cost += a_presses * a_button_cost + b_presses * b_button_cost
    else:
        print('Machine #%d cannot be won' % machine_number)

print('Part 1: All winnable machines can be won at a total cost of %d' % token_cost)

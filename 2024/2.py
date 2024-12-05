input_data = [
	"48 46 47 49 51 54 56",
	"1 1 2 3 4 5",
	"1 2 3 4 5 5",
	"5 1 2 3 4 5",
	"1 4 3 2 1",
	"1 6 7 8 9",
	"1 2 3 4 3",
	"9 8 7 6 7",
	"7 10 8 10 11",
	"29 28 27 25 26 25 22 20",
	"7 10 8 10 11",
	"29 28 27 25 26 25 22 20",
	"8 9 10 11"
]
input_data = open("2-input.txt", "r")

input = [[int(x) for x in line.split(" ")] for line in input_data]

def is_safe_transition(report_is_ascending, current, next):
	return current != next and \
		(report_is_ascending and next > current and next <= current + 3) or \
		(not report_is_ascending and next < current and next >= current - 3)

def report_is_safe(report):
	if len(report) < 2:
		return True
	
	is_ascending = report[0] < report[1]
	for (index, current) in enumerate(report[:-1]):
		next = report[index + 1]
		if not is_safe_transition(is_ascending, current, next):
			# print("Unsafe datapoint transition from %d to %d (problem at index %d)" % (current, next, index), report)
			return False

	return True

# Part 1
safe_report_count = 0
for report in input:
	if report_is_safe(report):
		safe_report_count += 1

print("Number of safe reports: %d of %d total reports were safe" % (safe_report_count, len(input)))

# Part 2
safe_report_count = 0
for report in input:
	is_already_safe = report_is_safe(report)
	if is_already_safe:
		safe_report_count += 1
		continue

	for index in range(len(report)):
		snipped = report[:index] + report[index+1:]
		is_safe = report_is_safe(snipped)
		# print(snipped, is_safe)
		if is_safe:
			safe_report_count += 1
			break

print("Number of safe reports with the Problem Dampener: %d of %d total reports were safe" % (safe_report_count, len(input)))

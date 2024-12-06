input_ordering_rules = [
	"47|53",
	"97|13",
	"97|61",
	"97|47",
	"75|29",
	"61|13",
	"75|53",
	"29|13",
	"97|29",
	"53|29",
	"61|53",
	"97|53",
	"61|29",
	"47|13",
	"75|47",
	"97|75",
	"47|61",
	"75|61",
	"47|29",
	"75|13",
	"53|13",
]
input_page_updates = [
	"75,47,61,53,29",
	"97,61,53,29,13",
	"75,29,13",
	"75,97,47,61,53",
	"61,13,29",
	"97,13,75,29,47",
]
input_ordering_rules = open("5-input-1.txt", "r")
input_page_updates = open("5-input-2.txt", "r")

ordering_rules = [[int(x) for x in rule.split("|")] for rule in input_ordering_rules]
page_antirequisites = {}
for ordering_rule in ordering_rules:
	if ordering_rule[0] not in page_antirequisites:
		page_antirequisites[ordering_rule[0]] = []
	
	page_antirequisites[ordering_rule[0]].append(ordering_rule[1])

bad_jobs = []

# Part 1
all_jobs = [[int(x) for x in update.split(",")] for update in input_page_updates]
good_job_middle_page_sum = 0
for page_update_job in all_jobs:
	# print("Checking job", page_update)
	pages_printed = set()
	is_bad_update = False

	for page in page_update_job:
		pages_printed.add(page)
		if page not in page_antirequisites:
			# Page has no ordering requirements
			continue

		antirequisites = page_antirequisites[page]

		# If any of this page's antirequisites have already been printed, this is a bad job
		if any(x in pages_printed for x in antirequisites):
			# print("--> Page %d cannot be printed; the following may not print before it:" % page, antirequisites)
			is_bad_update = True
			break
	
	if is_bad_update:
		bad_jobs.append(page_update_job)
	else:
		middle_page = page_update_job[int(len(page_update_job) / 2)]
		# print("Middle page of good job is", middle_page)
		good_job_middle_page_sum += middle_page

print("Part 1: Sum of middle page numbers of good jobs is %d" % good_job_middle_page_sum)

# Part 2
fixed_job_middle_page_sum = 0
for bad_job in bad_jobs:
	# print("Reordering bad job", bad_job)
	for index, page in enumerate(bad_job):
		if page not in page_antirequisites:
			# print("Page %d has no ordering requirements" % page)
			continue

		antirequisites = page_antirequisites[page]
		ordering_violations = list(set(antirequisites) & set(bad_job[:index]))
		if len(ordering_violations) == 0:
			# print("Page %d has no ordering violations" % page)
			continue

		# print("Page %d has ordering violations" % page, "against antirequisites", antirequisites, "in", bad_job)
		# print("--> Page %d needs to print before the following pages:" % page, ordering_violations)
		violation_indices = [bad_job.index(x) for x in ordering_violations]
		# print("--> Indices of violations", violation_indices)
		min_violation_index = min(violation_indices)
		del bad_job[index]
		bad_job.insert(min_violation_index, page)
		# print("--> Updated job order", bad_job)
	
	middle_page = bad_job[int(len(bad_job) / 2)]
	# print("Middle page of fixed job is", middle_page)
	fixed_job_middle_page_sum += middle_page

print("Part 2: Sum of middle page numbers of fixed jobs is %d" % fixed_job_middle_page_sum)
from report_repair import solution as solve

def test_report_repair_part1(n = 2):
	# Sample data given from problem
	given_example_data = (
		1721,
		979,
		366,
		299,
		675,
		1456,
	)
	test_cases = (
		(0, 2020),
		(1, 2019),
		(1010, 1010)
	)
	expectations = (
		0,
		2019,
		1020100
	)

	# Expected solution given from problem
	assert solve(given_example_data) == 514579
	
	# Expected results from own test data
	acc = 0
	for case in test_cases:
		assert solve(case, n) == expectations[acc]
		acc += 1

def test_report_repair_part2(n = 3):
	test_cases = (
		(0, 2020, 2019, 1),
		(1, 2019, 2018, 1),
		(673, 673, 674),
		(979, 366, 675)
	)
	expectations = (
		0,
		2018,
		305274146,
		241861950
	)

	# Expected results from own test data
	acc = 0
	for case in test_cases:
		assert solve(case, n) == expectations[acc]
		acc += 1

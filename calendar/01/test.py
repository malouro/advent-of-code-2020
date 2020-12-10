from solution import solution as run


def test_report_repair():
	# Sample data given from problem
	given_example_data = [
		1721,
		979,
		366,
		299,
		675,
		1456,
	]
	test_cases = [
		[0, 2020],
		[1, 2019],
		[1010, 1010]
	]
	expectations = [
		0,
		2019,
		1020100
	]

	# Expected solution given from problem
	assert run(given_example_data) == 514579
	
	# Expected results from own test data
	acc = 0
	for case in test_cases:
		assert run(case) == expectations[acc]
		acc += 1

from binary_boarding import get_seat_id, solve_part_1, solve_part_2

class TestBinaryBoarding:
	test_cases = [
		'BFFFBBFRRR',
		'FFFBBBFRRR',
		'BBFFBBFRLL'
	]
	expected_seat_ids = [567, 119, 820]

	def test__get_seat_id(self):
		acc = 0
		for board_pass in self.test_cases:
			assert(get_seat_id(board_pass)) == self.expected_seat_ids[acc]
			acc += 1

	def test__part_one(self):
		assert(solve_part_1(self.test_cases)) == 820

	def test__part_two(self):
		assert(solve_part_2(self.test_cases)) == 120

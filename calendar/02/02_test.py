from password_philosophy import solve as run_against_list
from password_philosophy import check_password
from password_philosophy import parse

class TestPasswordPolicyPartOne:
	policy = 1

	def test_with_list_data(self):
		example_data = (
			'1-3 a: abcde',
			'1-3 b: cdefg',
			'2-9 c: ccccccccc'
		)

		assert run_against_list(example_data, self.policy) == 2

	def test_unit(self):
		assert check_password(parse('1-3 a: abcde'), self.policy) == True
		assert check_password(parse('1-3 b: cdefg'), self.policy) == False
		assert check_password(parse('2-9 c: ccccccccc'), self.policy) == True


class TestPasswordPolicyPartTwo:
	policy = 2

	def test_with_list_data(self):
		example_data = (
			'1-3 a: abcde',
			'1-3 b: cdefg',
			'2-9 c: ccccccccc'
		)

		assert run_against_list(example_data, self.policy) == 1

	def test_unit(self):
		assert check_password(parse('1-3 a: abcde'), self.policy) == True
		assert check_password(parse('1-3 b: cdefg'), self.policy) == False
		assert check_password(parse('2-9 c: ccccccccc'), self.policy) == False


from custom_customs import solution, get_set_of_yes

class TestCustomCustoms:
	data = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

	def test__get_set_of_yes(self):
		# Intersect = False
		assert get_set_of_yes([
			'abcx',
			'abcy',
			'abcz',
		], False) == { 'a', 'b', 'c', 'x', 'y', 'z' }
		# Intersect = True
		assert get_set_of_yes([
			'abcx',
			'abcy',
			'abcz',
		], True) == { 'a', 'b', 'c' }

	def test__full_solution(self):
		# Intersect = False
		assert(solution(self.data)) == 11
		# Intersect = True
		assert(solution(self.data, True)) == 6

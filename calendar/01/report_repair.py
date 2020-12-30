import math
from os import path
from sys import argv
from itertools import combinations, dropwhile

TARGET_NUMBER = 2020

def solve(expenses, n_value = 2, target_num = TARGET_NUMBER):
	"""
	Returns product of the N amount of expenses that sum up to the given target number
	"""
	constraint = lambda x: sum(x) != target_num
	accepted_values = next(dropwhile(constraint, combinations(expenses, n_value)))
	return math.prod(accepted_values)


if __name__ == "__main__":
	del argv[0]
	# Defaults to n=2
	N = 2

	if path.isfile(argv[0]):
		print('Input file given; running report repair...')
		expense_report = list(map(int, open(argv[0]).read().split('\n')))
		if argv.__len__() > 1:
			N = int(argv[1])
			print(f'Given "n" value of {N} as the number of entries to summate')
		else:
			print(f'Using default "n" value of {N} as the number of entries to summate')

	else:
		print('Running report repair on given arguments.')
		expense_report = list(map(int, argv))
		N = argv[argv.__len__() - 1]
		print(f'Using last argument ({N}) for the "n" number of entries to summate)')

	report = solve(expense_report, N)
	print(report)

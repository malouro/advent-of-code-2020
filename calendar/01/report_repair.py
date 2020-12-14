import math
from os import path
from sys import argv
from itertools import combinations, dropwhile

def solution(expenses, n = 2):
	constraint = lambda x: sum(x) != 2020
	accepted_values = next(dropwhile(constraint, combinations(expenses, n)))
	return math.prod(accepted_values)

if __name__ == '__main__':
	del argv[0]
	# Defaults to n=2 for the Part One solution
	n = 2

	if path.isfile(argv[0]):
		print('Input file given; running report repair...')
		expenses = list(map(int, open(argv[0]).read().split('\n')))
		if argv.__len__() > 1:
			n = int(argv[1])
			print(f'Given "n" value of {n} as the number of entries to summate')
		else:
			print(f'Using default "n" value of {n} as the number of entries to summate')

	else:
		print('Running report repair on given arguments.')
		expenses = list(map(int, argv))
		n = argv[argv.__len__() - 1]
		print(f'Using last argument ({n}) for the "n" number of entries to summate)')

	report = solution(expenses, n)
	print(report)

import math
from os import path
from sys import argv
from itertools import combinations, dropwhile

def solution(expenses, n = 2):
	# "lambda"
	# dropwhile from itertools
	# combinations from itertools
	constraint = lambda x: sum(x) != 2020
	accepted_values = next(dropwhile(constraint, combinations(expenses, n)))
	return math.prod(accepted_values)


if __name__ == '__main__':
	del argv[0]
	# Defaults to n=2 for the Part One solution
	n = 2

	if path.isfile(argv[0]):
		expenses = list(map(int, open(argv[0]).read().split('\n')))
	else:
		expenses = list(map(int, argv))
	if argv.__len__() > 1:
		n = int(argv[1])

	report = solution(expenses, n)
	print(report)

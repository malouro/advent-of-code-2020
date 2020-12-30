import functools
from sys import argv

def get_set_of_yes(group, intersection=False):
	"""
	Given a group of responses - figure out the set of
	questions that were responded to with "yes"

	(This assumes that each element of `group` contains only
	questions that had "yes" responses -- a constraint given with
	the original puzzle)
	"""
	return set(''.join(group)) if not intersection else (
		functools.reduce(
			lambda a,b: set(a).intersection(b),
			group,
		)
	)

def reduce_responses(data_set, intersection=False):
	"""
	Iterate through and count up number "yes" responses given from every group

	When `intersection` = `True`, this will take into account the same "yes"
	responses from each member of each group
	"""
	return functools.reduce(
		lambda a,b: a + b,
		list(map(
			lambda group: get_set_of_yes(group, intersection).__len__(),
			data_set
		)),
		0
	)

def parse_data(data):
	"""
	Parses input data into usable `group`s of "yes" responses
	"""
	return list(
		map(
			lambda x: x.split('\n'),
			data.split('\n\n')
		)
	)

def solution(input_data, get_same_responses_only=False):
	"""
	Returns the solution!

	If `get_same_responses_only` is `True` this will return the part two solution.
	"""
	return reduce_responses(
		parse_data(open(input_data).read()),
		get_same_responses_only
	)


if __name__ == "__main__":
	del argv[0]

	input_data_file = argv[0] if argv.__len__() > 0 else './input.txt'
	solution_part = int(argv[1]) if argv.__len__() > 1 else 1

	if solution_part == 1:
		print(solution(input_data_file, False))
	else:
		print(solution(input_data_file, True))

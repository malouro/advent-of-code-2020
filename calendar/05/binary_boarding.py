from sys import argv
from os import path

def get_seat_id(board_pass):
	"""
	Returns the seat id for a given boarding pass number
	"""
	return int(''.join(list(map(lambda x: '1' if x in 'BR' else '0', board_pass))), 2)

def get_seat_ids(board_passes):
	"""
	Returns a list of seat IDs for a given list of boarding passes
	"""
	return [get_seat_id(x) for x in board_passes]

def solve_part_1(board_passes):
	"""Return Part 1 solution for given input data"""
	return max(get_seat_ids(board_passes))

def solve_part_2(board_passes):
	"""Return Part 2 solution for given input data"""
	seats = get_seat_ids(board_passes)
	return next(filter(lambda x: x not in seats, range(min(seats), max(seats))))


if __name__ == "__main__":
	# Usage:
	# binary_boarding <input_file> <part?(1,2)>

	del argv[0]

	if path.isfile(argv[0]):
		input_data = open(argv[0]).read().split('\n')
	else:
		raise Exception('Bad input data, or file doesn\'t exist.')

	if not argv[1] or argv[1] == '1':
		print(solve_part_1(input_data))
	elif argv[1] == '2':
		print(solve_part_2(input_data))

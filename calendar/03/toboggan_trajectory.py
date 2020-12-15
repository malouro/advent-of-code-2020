import math
from os import path
from sys import argv

# List of variable defaults
SLOPE_R = 3
SLOPE_D = 1
TREE_CHAR = '#'
TREE_COUNT = 0

def toboggan(mountain_map, pos, slope_r = SLOPE_R, slope_d = SLOPE_D, tree_count = TREE_COUNT):
	"""
	Keep tobogganing down the mountain. ⛷

	- area_map: 2d list of the map
	- pos: current [x, y] position
	- tree_count: number of trees encountered so far
	- slope_r: rightward slope
	- slope_d: downwards slope

	Recurse if bottom of map isn't reached yet.
	Once at the bottom - return the `tree_count` value. :)
	"""
	width = mountain_map[pos[0]].__len__() - 1

	if mountain_map[pos[0]][pos[1]] == TREE_CHAR:
		print('Tree found! 🌲')
		tree_count += 1

	# Check if at bottom of map
	if mountain_map.__len__() <= (pos[0] + slope_d):
		# This is when we know to end the toboggan ride
		return tree_count

	# Ride down!
	new_pos = [pos[0] + slope_d, pos[1] + slope_r]
	if new_pos[1] > width:
		new_pos[1] = (new_pos[1] % width) - 1

	print(f'Moving to new position @ {new_pos[0]}, {new_pos[1]}')

	# Recurse
	return toboggan(
		mountain_map,
		new_pos,
		slope_r,
		slope_d,
		tree_count
	)

def check_list_of_slopes(mountain_map, slopes):
	"""
	Returns list of tree collisions for all slopes given
	"""
	tree_collisions = []
	for slope in slopes:
		tree_collisions.append(
			toboggan(mountain_map, (0,0), slope[0], slope[1])
		)
	return tree_collisions

def solve_part_1(mountain_map):
	"""Solves part 1, given a map"""
	return toboggan(mountain_map, (0, 0), 3, 1)

def solve_part_2(mountain_map):
	"""Solves part 2, given a map and a list of slopes"""
	return math.prod(
		check_list_of_slopes(mountain_map, (
			(1, 1),
			(3, 1),
			(5, 1),
			(7, 1),
			(1, 2)
		))
	)

if __name__ == "__main__":
	del argv[0]

	if argv.__len__() > 0:
		if path.isfile(argv[0]):
			data = list(map(str, open(argv[0]).read().split('\n')))
		else:
			raise Exception('Bad data, check your input file.')
	else:
		raise Exception('No args given.')

	print(solve_part_1(data))
	print(solve_part_2(data))

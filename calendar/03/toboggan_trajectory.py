from os import path
from sys import argv

SLOPE_R = 3
SLOPE_D = 1
TREE_CHAR = '#'
TREE_COUNT = 0

def toboggan(area_map, pos, tree_count = 0, slope_r = SLOPE_R, slope_d = SLOPE_D):
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
	width = area_map[pos[0]].__len__() - 1

	if area_map[pos[0]][pos[1]] == TREE_CHAR:
		print('Tree found! 🌲')
		tree_count += 1

	# Check if at bottom of map
	if area_map.__len__() <= (pos[0] + slope_d):
		# This is when we know to end the toboggan ride
		return tree_count

	# Ride down!
	new_pos = [pos[0] + slope_d, pos[1] + slope_r]
	if new_pos[1] > width:
		new_pos[1] = (new_pos[1] % width) - 1

	print(f'Moving to new position @ {new_pos[0]}, {new_pos[1]}')

	# Recurse
	return toboggan(
		area_map,
		new_pos,
		tree_count
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

	print(toboggan(data, [0, 0]))

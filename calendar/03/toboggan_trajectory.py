from os import path
from sys import argv

slope_r = 3
slope_d = 1
tree_char = '#'
tree_count = 0

def check_slope(area_map, pos, r = slope_r, d = slope_d):
	global tree_count, tree_char

	width = area_map[pos[0]].__len__() - 1

	if area_map[pos[0]][pos[1]] == tree_char:
		print(f'Tree found! 🌲')
		tree_count += 1

	# Check if at bottom of map
	if (
		area_map.__len__() <= (pos[0] + d)
	):
		# This is when we know to end the toboggan ride
		return tree_count

	# Ride down!
	new_pos = [pos[0] + d, pos[1] + r]
	if new_pos[1] > width:
		new_pos[1] = (new_pos[1] % width) - 1

	print(f'Moving to new position @ {new_pos[0]}, {new_pos[1]}')

	# Recurse
	return check_slope(
		area_map,
		new_pos
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

	print(check_slope(data, [0, 0]))

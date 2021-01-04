from sys import argv

bags_set = set()

def get_parent_bags(child_bag, bags_dict):
	"""
	Check thru bags dictionary and returns list of viable
	parents (containing bags) for the given child bag
	"""
	for parent in bags_dict:
		content = bags_dict[parent]
		if child_bag in content:
			bags_set.add(parent)
			get_parent_bags(parent, bags_dict)
	return

def parse_data(data):
	"""
	Creates dictionary of bags based on input data
	"""
	bags_dict = {}
	bags = data.split('\n')

	for bag in bags:
		bag = bag.replace(' bags', '').replace('.', '').split(' contain ')
		bags_dict[bag[0]] = bag[1]

	return bags_dict

def solution_part_one(input_data, target_bag = 'shiny gold'):
	"""
	Gives solution for part 1
	"""
	bags_dict = parse_data(input_data)

	get_parent_bags(target_bag, bags_dict)

	return bags_set

def solution_part_two(input_data):
	"""
	Gives solution for part 2
	"""
	print(input_data)
	return 'WIP'


if __name__ == "__main__":
	del argv[0]

	input_data_file = argv[0] if argv.__len__() > 0 else './input.txt'
	solution_part = int(argv[1]) if argv.__len__() > 1 else 1

	if solution_part == 1:
		solution = solution_part_one(open(input_data_file).read())
		print(solution.__len__())
	else:
		print(solution_part_two(open(input_data_file).read()))

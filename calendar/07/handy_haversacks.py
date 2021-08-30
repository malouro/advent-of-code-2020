from sys import argv
import re

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

def get_child_bags(parent_bag, bags_dict):
	"""
	What bags are contained within the given parent?
	"""
	total_bag_count = 0
	bags = bags_dict[parent_bag].split(',') if parent_bag is not None else []

	for bag in bags:
		print(bag)
		count_match = re.search(r'\d+', bag)

		print(count_match)

		if count_match is None:
			count = 0
			bag = None
		else:
			count = count_match.group(0)
			bag = bag.replace(count + ' ', '')

		total_bag_count += (int(count) * get_child_bags(bag, bags_dict)) + int(count)

	return total_bag_count


def parse_data(data):
	"""
	Creates dictionary of bags based on input data
	"""
	bags_dict = {}
	bags = data.split('\n')

	for bag in bags:
		bag = re.sub(r' bags*', '', bag).replace('.', '').split(' contain ')
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
	bags_dict = parse_data(input_data)

	return get_child_bags('shiny gold', bags_dict)


if __name__ == "__main__":
	del argv[0]

	input_data_file = argv[0] if argv.__len__() > 0 else './input.txt'
	solution_part = int(argv[1]) if argv.__len__() > 1 else 1

	if solution_part == 1:
		solution = solution_part_one(open(input_data_file).read())
		print(solution)
		print(solution.__len__())
	else:
		print(solution_part_two(open(input_data_file).read()))

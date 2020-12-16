from os import path
from sys import argv
import re

REQUIRED_FIELDS = [
	'byr',
	'ecl',
	'eyr',
	'hcl',
	'hgt',
	'iyr',
	'pid'
]

def parse_passport(passport):
	"""
	Parses a single passport for all necessary info.
	Returns `True` for a valid passport.
	"""
	data_points = re.split(r'\n|\s+', passport)
	fields = sorted(list(map(lambda x : x[:3], data_points)))

	if 'cid' in fields:
		fields.remove('cid')
	if fields == REQUIRED_FIELDS:
		return True
	return False

def validate_passports(passport_data):
	"""
	Determines how many valid passports exist in a full list
	of passport data.
	"""
	passports = list(passport_data.split('\n\n'))
	valid_count = 0

	for passport in passports:
		if parse_passport(passport):
			valid_count += 1
	return valid_count

if __name__ == "__main__":
	del argv[0]

	if path.isfile(argv[0]):
		input_data = open(argv[0]).read()
	else:
		raise Exception('Bad input data, or file doesn\'t exist.')

	print(validate_passports(input_data))

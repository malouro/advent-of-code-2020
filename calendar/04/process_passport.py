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

MIN_BIRTH_YEAR = 1920
MAX_BIRTH_YEAR = 2002

MIN_ISSUE_YEAR = 2010
MAX_ISSUE_YEAR = 2020

MIN_EXP_YEAR = 2020
MAX_EXP_YEAR = 2030

MIN_HEIGHT_CM = 150
MAX_HEIGHT_CM = 193
MIN_HEIGHT_IN = 59
MAX_HEIGHT_IN = 76

POSSIBLE_EYE_COLORS = 'amb|blu|brn|gry|grn|hzl|oth'

def parse_field(field):
	"""
	Parses a field from the passport.
	Returns `True` for a valid passport field entry.

	> Note: A `field` must be a tuple/list of two elements: the field `type` and the field's `value`
	"""
	field_type = field[0]
	field_value = field[1]

	# Birth Year
	if field_type == 'byr':
		return MIN_BIRTH_YEAR <= int(field_value) <= MAX_BIRTH_YEAR
	# Issue Year
	if field_type == 'iyr':
		return MIN_ISSUE_YEAR <= int(field_value) <= MAX_ISSUE_YEAR
	# Expiration Year
	if field_type == 'eyr':
		return MIN_EXP_YEAR <= int(field_value) <= MAX_EXP_YEAR
	# Height (No dwarves or basketball players allowed, apparently)
	if field_type == 'hgt':
		if 'cm' in field_value:
			return MIN_HEIGHT_CM <= int(field_value[:-2]) <= MAX_HEIGHT_CM
		if 'in' in field_value:
			return MIN_HEIGHT_IN <= int(field_value[:-2]) <= MAX_HEIGHT_IN
		return False
	# Hair Color (no rgb or hsl hair, alright?)
	if field_type == 'hcl':
		return bool(re.fullmatch('#[0-9A-Fa-f]{6}', field_value))
	# Eye color
	if field_type == 'ecl':
		return bool(re.fullmatch(POSSIBLE_EYE_COLORS, field_value))
	# Passport ID
	if field_type == 'pid':
		return bool(re.fullmatch('[0-9]{9}', field_value))
	return False

def parse_passport(passport):
	"""
	Parses a single passport for all necessary info.
	Returns `True` for a valid passport.
	"""
	data_points = re.split(r'[\n\s]+', passport)
	fields = list(map(lambda x: ( x[:3], x[4:] ), data_points))
	cid_el = None
	i = 0

	for field in fields:
		# Remember where `cid` was
		if field[0] == 'cid':
			cid_el = field
			continue
		# Parse field and its value
		if not parse_field(field):
			print(f'Field failed: {field} ❌')
			return False
		i += 0

	# Remove `cid` if it exists
	if cid_el is not None:
		fields.remove(cid_el)

	# Now check that the fields supplied match requirements
	fields_given = sorted(list(map(lambda x: x[0], fields)))
	valid_passport = fields_given == REQUIRED_FIELDS

	if valid_passport:
		print(f'Passport valid: {passport} ✅')
	else:
		print(f'Passport invalid: {fields_given} ❌')
	return valid_passport

def validate_passports(passport_data):
	"""
	Determines how many valid passports exist in a full list
	of passport data.
	"""
	passports = list(passport_data.split('\n\n'))
	print(f'Total passports to parse: {passports.__len__()}')
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

	print(f'Valid passports: {validate_passports(input_data)}')

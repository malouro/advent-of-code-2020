from os import path
from sys import argv

VALID_PASSWORD_POLICIES = (1, 2)

def parse(string_input):
	"""
	Parse info from given password data.
	[ requirement, letter_to_check_for, password]

	```py
	# This:
	parse("1-3 a: abcde")

	# Returns:
	{ 'item': ['1-3', 'a:', 'abcde'],
	'req': [1, 3],
	'letter': 'a',
	'password': 'abcde' }
	```
	"""
	item = string_input.split(' ')

	return {
		'item': item,
		'req': list(map(int, item[0].split('-'))),
		'letter': item[1][0],
		'password': item[2]
	}

def check_password(data, policy):
	"""
	Implement password policy against given password data.
	Returns `True` for valid password, `False` for invalid.

	**Policy 1:**
	X-Y ranged occurrences of a given letter must exist within the password.

	**Policy 2:**
	Letter must exist at one, and **only** one, of the positions given with
	(non-zero indexed) `{data.req}`

	Eg:
	```
	'1-3 a: abcdef' # Passes because 'a' exists at (1) and NOT (3)
	'1-5 c: cccccc' # Fails because 'c' exists at BOTH (1) and (3)
	'1-3 f: eeeeee' # Fails because 'f' does NOT exist at (1) OR (3)
	```
	"""
	item = data['item']
	req = data['req']
	letter = data['letter']
	password = data['password']

	if policy == VALID_PASSWORD_POLICIES[0]:
		count = 0
		for char in password:
			if char == letter:
				if count == req[1]:
					count = 0
					break
				count += 1
		if count >= req[0]:
			print(f'Valid pass found! {item}')
			return True
		return False

	if policy == VALID_PASSWORD_POLICIES[1]:
		if (password[req[0] - 1] == letter) != (password[req[1] - 1] == letter):
			print(f'Valid pass found! {item}')
			return True
		return False

	# policy number not supported
	return Exception(
		f'Invalid password policy {policy} given.' +
		f'Valid options include: {VALID_PASSWORD_POLICIES}'
	)

def solve(password_data, policy):
	"""
	Offer solution given a list of password data & the password policy number to use.
	"""
	valid_passes = 0

	for item in password_data:
		parsed_data = parse(item)
		if check_password(parsed_data, policy):
			valid_passes += 1

	return valid_passes


if __name__ == "__main__":
	del argv[0]
	POLICY = 1

	if path.isfile(argv[0]):
		input_data = list(map(str, open(argv[0]).read().split('\n')))
		if argv.__len__() > 1:
			POLICY = int(argv[1])
			print(f'Using given policy number of {POLICY}.')
	else:
		raise Exception('Bad data, check your input file.')

	RESULTS = solve(input_data, POLICY)
	print(f'✅ Valid password total: {RESULTS}')

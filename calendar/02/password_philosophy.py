from os import path
from sys import argv

def solution(data):
	# Number of valid passwords
	valid_passes = 0

	for item in data:
		item = item.split(' ')
		count = 0

		# Parse info from data...
		# [ requirement, letter to check for, password]
		# ie:
		# [ '1-3', 'a:', 'abcde' ] => passes, valid_passes++
		req = list(map(int, item[0].split('-')))
		letter = item[1][0]
		password = item[2]

		# Check the password!
		for char in password:
			if char == letter:
				if count == req[1]:
					count = 0
					break
				count += 1

		if count >= req[0]:
			valid_passes += 1
			print(f'Valid pass found! {item}')

	return valid_passes


if __name__ == "__main__":
	del argv[0]

	if path.isfile(argv[0]):
		data = list(map(str, open(argv[0]).read().split('\n')))
	else:
		raise Exception('Bad data, check your input file.')

	print(f'Valid password total: {solution(data)}')

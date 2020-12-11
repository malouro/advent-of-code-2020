from password_philosophy import solution as run

def test_password_philosophy():
	example_data = [
		'1-3 a: abcde',
		'1-3 b: cdefg',
		'2-9 c: ccccccccc'
	]

	result = run(example_data)
	print(result)
	assert result == 2


if __name__ == "__main__":
	test_password_philosophy()
	pass

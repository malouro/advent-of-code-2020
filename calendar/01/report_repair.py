from os import path
from sys import argv

def solution(data, target_num = 2020):
	for num in data:
		rest_nums = data.copy()
		del rest_nums[rest_nums.index(num)]

		for cur_num in rest_nums:
			if num + cur_num == target_num:
				answer = num * cur_num

				print(f'Found it!\n{num} + {cur_num} = 2000')
				print(f'{num} * {cur_num} = {answer}')

				return answer

	return None


if __name__ == "__main__":
	del argv[0]

	if path.isfile(argv[0]):
		data = list(map(int, open(argv[0]).read().split('\n')))
	else:
		data = list(map(int, argv))

	print(solution(data))

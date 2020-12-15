from toboggan_trajectory import toboggan, check_list_of_slopes 
import math

class TestTobogganTrajectory:
	test_map_1 = (
		'..##.......',
		'#...#...#..',
		'.#....#..#.',
		'..#.#...#.#',
		'.#...##..#.',
		'..#.##.....',
		'.#.#.#....#',
		'.#........#',
		'#.##...#...',
		'#...##....#',
		'.#..#...#.#'
	)

	def test_single_slope(self):
		result = toboggan(
			self.test_map_1,
			(0,0),
			3,
			1
		)
		assert result == 7

	def test_lists_of_slopes(self):
		tree_collisions = check_list_of_slopes(
			self.test_map_1,
			(
				(1,1),
				(3,1),
				(5,1),
				(7,1),
				(1,2)
			)
		)
		assert math.prod(tree_collisions) == 336

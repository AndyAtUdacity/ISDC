from localization_v1 import initialize_beliefs, sense, move
from localization_v2 import Robot


def close_enough(g1, g2):
	for r1, r2 in zip(g1,g2):
		for v1, v2 in zip(r1, r2):
			if abs(v1 - v2) > 0.001:
				return False
	return True

EXAMPLE_GRID = [
	['r', 'g', 'r', 'r', 'r', 'g'],
	['g', 'g', 'r', 'r', 'g', 'g'],
	['r', 'r', 'r', 'g', 'r', 'g'],
	['g', 'g', 'r', 'g', 'r', 'r'],
	['r', 'r', 'g', 'r', 'r', 'g'],
]

def test_functions():
	# test initialization
	grid = EXAMPLE_GRID
	beliefs = initialize_beliefs(EXAMPLE_GRID)
	expected = [[1.0/30 for i in range(6)] for j in range(5)]
	assert close_enough(beliefs, expected)

	# test relative probabilities after sense
	p_hit = 3.0
	p_miss = 1.0
	beliefs = sense('r', grid, beliefs)
	assert abs(beliefs[0][0] - 3* beliefs[0][1]) < 0.001

	# test normalization / total probability after sense
	total = 0.0
	for row in beliefs:
		for cell in row:
			total += cell
	assert abs(total - 1.0) < 0.001

	# TODO test move
	print "functions passed"

def test_class():
	# TODO add tests
	robot = Robot(EXAMPLE_GRID)
	robot.sense('r')
	print robot.beliefs
	print 'class passed'

test_functions()
test_class()
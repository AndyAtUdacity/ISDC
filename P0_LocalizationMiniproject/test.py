from localization_v1 import initialize_beliefs, sense, move
from localization_v2 import Robot
from helpers import is_robot_localized
import random
from matplotlib import pyplot as plt
import maps
import time
import pdb


def close_enough(g1, g2):
	for r1, r2 in zip(g1,g2):
		for v1, v2 in zip(r1, r2):
			if abs(v1 - v2) > 0.001:
				return False
	return True





# EXAMPLE_GRID = [
# 	['r','r','r'],
# 	['g','g','g'],
# 	['r','r','r']
# ]

def test_functions():
	# test initialization
	grid = EXAMPLE_GRID
	beliefs = initialize_beliefs(EXAMPLE_GRID)
	expected = [[1.0/30 for i in range(6)] for j in range(5)]
	assert close_enough(beliefs, expected)

	# test relative probabilities after sense
	beliefs = sense('r', grid, beliefs)
	assert abs(beliefs[0][0] - p_hit/p_miss* beliefs[0][1]) < 0.001

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

def simulate_motion(grid,p_hit=3.0,p_miss=1.0, blurring=0.1,visualize=False,N=5000):

	beliefs = initialize_beliefs(grid)
	height = len(grid)
	width = len(grid[0])
	y_mid = height / 2
	x_mid = width / 2
	true_pos = (y_mid, x_mid)
	found = False
	prob_wrong = p_miss / (p_hit + p_miss)
	if visualize:
		plt.ion()
		X = []
		Y = []
		sizes = []
	for i in range(N):
		localized = is_robot_localized(beliefs, true_pos)
		if localized == False and visualize == True:
			print "robot thinks it knows where it is but its wrong. (timestep {})".format(i)
			raw_input("> press enter to continue")
		if localized == True:
			if not visualize:
				return i
			if not found:
				print "robot is localized! (timestep {})".format(i)
				raw_input("> press enter to continue")
				found = True
		true_color = grid[true_pos[0]][true_pos[1]]
		color = true_color
		if random.random() < prob_wrong:
			# print "BAD SENSE!"
			if color == 'r': 
				color = 'g'
			else:
				color = 'r'

		beliefs = sense(color, grid, beliefs,p_hit,p_miss)
		
		if visualize:
			# empty lists of existing data
			del(X[:])
			del(Y[:])
			del(sizes[:])
			for y, row in enumerate(beliefs):
				for x, belief in enumerate(row):
					X.append(x)
					Y.append(height-y-1)
					sizes.append(1000.0 * belief)
			plt.clf()
			plt.scatter(X,Y,s=sizes)
			plt.scatter([true_pos[1]], [height-true_pos[0]-1], color='red')
			plt.draw()
			time.sleep(0.1)
		dx = random.choice([-1,0,1])
		dy = random.choice([-1,0,1])
		x = (true_pos[1] + dx) % width
		y = (true_pos[0] + dy) % height
		true_pos = (y, x)
		beliefs = move(dy, dx, beliefs, blurring)

def simulate(grid,p_hit=3.0,p_miss=1.0, blurring=0.1,visualize=False,N=5000):

	beliefs = initialize_beliefs(grid)
	height = len(grid)
	width = len(grid[0])
	y_mid = height / 2
	x_mid = width / 2
	true_pos = (y_mid, x_mid)
	found = False
	prob_wrong = p_miss / (p_hit + p_miss)

	for i in range(N):
		localized = is_robot_localized(beliefs, true_pos)

		true_color = grid[true_pos[0]][true_pos[1]]
		color = true_color
		if random.random() < prob_wrong:
			# print "BAD SENSE!"
			if color == 'r': 
				color = 'g'
			else:
				color = 'r'

		beliefs = sense(color, grid, beliefs,p_hit,p_miss)
		
		if visualize:
			# empty lists of existing data
			del(X[:])
			del(Y[:])
			del(sizes[:])
			for y, row in enumerate(beliefs):
				for x, belief in enumerate(row):
					X.append(x)
					Y.append(height-y-1)
					sizes.append(1000.0 * belief)
			plt.clf()
			plt.scatter(X,Y,s=sizes)
			plt.scatter([true_pos[1]], [height-true_pos[0]-1], color='red')
			plt.draw()
			time.sleep(0.1)
		dx = random.choice([-1,0,1])
		dy = random.choice([-1,0,1])
		x = (true_pos[1] + dx) % width
		y = (true_pos[0] + dy) % height
		true_pos = (y, x)
		beliefs = move(dy, dx, beliefs, blurring)

# test_functions()
# test_class()

# simulate_motion(EXAMPLE_GRID, visualize=True)
# simulate_motion(maps.ALMOST_PERIODIC,visualize=True)
# simulate_motion(maps.TARGET, visualize=True, blurring=0.5)


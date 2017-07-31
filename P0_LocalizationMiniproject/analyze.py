from localization_v1 import initialize_beliefs, sense, move

from test import simulate_motion
from maps import TARGET, PERIODIC, ALMOST_PERIODIC, RANDOM, biased_map
from numpy import mean,std

def get_avg_steps_til_localized(grid, p_hit, p_miss, blurring, N=20):
	height = len(grid)
	width = len(grid[0])
	y_mid = height / 2
	x_mid = width / 2
	true_pos = (y_mid, x_mid)
	found = False
	prob_wrong = p_miss / (p_hit + p_miss)

	num_steps = []
	for i in range(N):
		count = simulate_motion(grid,p_hit,p_miss,blurring,False)
		num_steps.append(count)
	return mean(num_steps), std(num_steps)

def compare_params(grid, param_list):
	averages = []
	for p_hit, p_miss, blurring in param_list:
		avg, std = get_avg_steps_til_localized(grid, p_hit, p_miss, blurring)
		averages.append(avg)

		print "average is {} +/- {}".format(avg, std)
		print "p_hit:     {}".format(p_hit)
		print "p_miss:    {}".format(p_miss)
		print "blurring:  {}".format(blurring)
		print
	return averages


def compare_maps(grids, params):
	averages = []
	p_hit, p_miss, blurring = params
	for grid in grids:
		avg, std = get_avg_steps_til_localized(grid, p_hit, p_miss, blurring)
		averages.append(avg)
		print "average is {} +/- {}".format(avg, std)
		print "for {} by {} grid".format(len(grid), len(grid[0]))
		print

def compare_map_sizes(sizes, params, N=20):
	averages = []
	p_hit, p_miss, blurring = params
	for size in sizes:
		size_avgs = []
		for i in range(N):
			grid = RANDOM(size)
			avg, sig = get_avg_steps_til_localized(grid, p_hit, p_miss, blurring, N=1)
			size_avgs.append(avg)
		avg = mean(size_avgs)
		sigma = std(size_avgs)
		averages.append(avg)
		print "average is {} +/- {}".format(avg, sigma)
		print "for {} by {} grid".format(len(grid), len(grid[0]))
		print

change_blur_param = [
	(3.0, 1.0, 0.001),
	(3.0, 1.0, 0.005),
	(3.0, 1.0, 0.01),
	(3.0, 1.0, 0.05),
	(3.0, 1.0, 0.1),
	(3.0, 1.0, 0.2),
	(3.0, 1.0, 0.3),
]

change_p_hit_param = [
	# (100.0,1.0, 0.1),
	# (50.0, 1.0, 0.1),
	(25.0, 1.0, 0.1),
	(15.0, 1.0, 0.1),
	(5.0,  1.0, 0.1),
	(5.0,  1.0, 0.1),
	(3.0,  1.0, 0.1),
	(2.5,  1.0, 0.1)
	# (2.0,  1.0, 0.1),
	# (1.5,  1.0, 0.1),

]

# compare_params(PERIODIC, change_p_hit_param)
# compare_params(ALMOST_PERIODIC, change_p_hit_param)
# grids = [RANDOM(size) for size in [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]]

# sizes = [5,10,20,30,40,50,75,100,150,200]
# compare_map_sizes(sizes, (10.0,1.0,0.05))

# grids = []
# for p_red in [0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02]:
# 	grid = biased_map(30, p_red)
# 	grids.append(grid)

# compare_maps(grids, (10.0,1.0,0.05))

G = RANDOM(20)
p_miss = 1.0
blurrings = [.04 * ( 1.5 ** j ) for j in range(6)]
p_hits = [3.0 * ( 1.5 ** i ) for i in range(9)]
data_grid = []
for p_hit in p_hits:
	data_row = []
	for blurring in blurrings:
		# print "p_hit:     {}".format(p_hit)
		# print "blurring:  {}".format(blurring)
		avg, sigma = get_avg_steps_til_localized(G, p_hit, p_miss, blurring,N=10)
		# print "average is {} +/- {}".format(avg, sigma)
		# print
		data_row.append((avg, sigma))
		print [str(d[0])[:6] for d in data_row]
	data_grid.append(data_row)

print
print [str(b)[:6] for b in blurrings]
for row in zip(data_grid,p_hit):
	print str([str(d[0])[:6] for d in row]) + str(p_hit)



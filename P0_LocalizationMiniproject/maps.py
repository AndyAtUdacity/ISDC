import random

R = 'r'
_ = 'g'
B = 'b'


SMALL_GRID = [
	[R,_,_],
	[_,R,R],
	[R,_,R],
]

MEDIUM_GRID = [
	[_,R,_,_,_,_],
	[_,R,_,_,_,R],
	[R,_,R,_,_,_],
	[_,_,R,R,_,_],
	[_,R,_,_,_,_],
	[_,_,R,R,_,_],
]

STRIPES = [
	[_,R,R,_,R,R,_,R,R],
	[R,R,_,R,R,_,R,R,_],
	[R,_,R,R,_,R,R,_,R],
	[_,R,R,_,R,R,_,R,R],
	[R,R,_,R,R,_,R,R,_],
	[R,_,R,R,_,R,R,_,R],
	[_,R,R,_,R,R,_,R,R],
	[R,R,_,R,R,_,R,R,_],
	[R,_,R,R,_,R,R,_,R],
]

PERIODIC = [
	[_,_,_,_,_,_,_,_],
	[_,R,_,_,_,R,_,_],
	[_,_,_,_,_,_,_,_],
	[_,_,_,R,_,_,_,R],
	[_,_,_,_,_,_,_,_],
	[_,R,_,_,_,R,_,_],
	[_,_,_,_,_,_,_,_],
	[_,_,_,R,_,_,_,R],
]

ALMOST_PERIODIC = [
	[_,_,_,_,_,_,_,_],
	[R,R,_,_,_,R,_,_],
	[_,_,_,_,_,_,_,_],
	[_,_,_,R,_,_,_,R],
	[_,_,_,_,_,_,_,_],
	[_,R,_,_,_,R,_,_],
	[_,_,_,_,_,_,_,_],
	[_,_,_,R,_,_,_,R],
]

TARGET = [
	[R,R,R,R,R,R,R,R,R],
	[R,_,_,_,_,_,_,_,R],
	[R,_,R,R,R,R,R,_,R],
	[R,_,R,_,_,_,R,_,R],
	[R,_,R,_,R,_,R,_,R],
	[R,_,R,_,_,_,R,_,R],
	[R,_,R,R,R,R,R,_,R],
	[R,_,_,_,_,_,_,_,R],
	[R,R,R,R,R,R,R,R,R],

]

ONE_RED = [
	[_,_,_,_,_,_,_],
	[_,_,_,_,_,_,_],
	[_,_,_,_,_,_,_],
	[_,_,_,_,_,_,_],
	[_,_,_,_,_,_,_],
	[_,_,_,_,_,_,_],
	[_,_,_,_,_,_,R],
]

HUGE = [
	[random.choice([R,_]) for i in range(50)] for j in range(50)
]

def RANDOM(size):
	return [[random.choice([R,_,B]) for i in range(size) ] for j in range(size)]

def biased_map(size, p_red):
	G = []
	for i in range(size):
		row = []
		for j in range(size):
			if random.random() < p_red:
				row.append(R)
			else:
				row.append(_)
		G.append(row)
	# for row in G:
	# 	print row
	return G
# import modules
import random
import numpy as np

def fire_spread(p, N, iter=1):
	'''
	This function returns the average ratio of 3(burnt) in N squared area

	Params
	-------------------
		p: percentage of area with tree (float, 0 to 1)
		N: width, length (int)
		iter: number of experiments to be averaged (int)

	Returns
	-------------------
		avg_score: average ratio of 3 (float)
	'''

	i = 1
	scores = []
	while i <= iter:
		# initialize trees
		T = N * N
		tree = np.zeros((T, N, N))
		for x in range(0, N):
			for y in range(0, N):
				tree[0, x, y] = random.choices([0, 1], [1-p, p])[0]

		# apply first fire
		x1 = random.randint(0, N-1)
		y1 = random.randint(0, N-1)
		tree[1, :, :] = tree[0, :, :].copy()
		tree[1, x1, y1] = 2

		# apply rules
		count_2 = [np.count_nonzero(tree[1, :, :] == 2)]
		t = 2
		while count_2[-1] != 0:
			tree[t, :, :] = tree[t-1, :, :].copy()
			for x in range(0, N):
				for y in range(0, N):
					if tree[t-1, x, y] == 2:
						tree[t, x, y] = 3
					elif tree[t-1, x, y] == 1:
						try:
							if tree[t-1, x-1, y] == 2:
								if x-1 >= 0:
									tree[t, x, y] = 2
						except IndexError:
							pass
						try:
							if tree[t-1, x+1, y] == 2:
								tree[t, x, y] = 2
						except IndexError:
							pass
						try:
							if tree[t-1, x, y-1] == 2:
								if y-1 >= 0:
									tree[t, x, y] = 2
						except IndexError:
							pass
						try:
							if tree[t-1, x, y+1] == 2:
								tree[t, x, y] = 2
						except IndexError:
							pass
              
			count_2.append(np.count_nonzero(tree[t, :, :] == 2))
			t += 1
		score = np.count_nonzero(tree[t-1, :, :] == 3) / (N * N)
		scores.append(score)
		
		i += 1

	# calculate average scores
	avg_score = sum(scores) / len(scores)
	return avg_score

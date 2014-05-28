#!/usr/local/bin/python2.7
import sys
import os

def optimal_bst(p, q):
	n = len(p)
	e = [[0 for i in range(n)] for i in range(n + 1)]
	w = [[0 for i in range(n)] for i in range(n + 1)]
	root = [[0 for i in range(n)] for i in range(n)]

	for i in range(1, n + 1):
		e[i][i - 1] = q[i - 1]
		w[i][i - 1] = q[i - 1]

	for length in range(1, n ):
		for i in range(1, n - length + 1):
			j = i + length - 1
			e[i][j] = 9999
			w[i][j] = w[i][j - 1] + p[j] + q[j]
			for r in range(i, j + 1):
				val = e[i][r - 1] + e[r + 1][j] + w[i][j]
				if e[i][j] > val:
					e[i][j] = val
					root[i][j] = r
				
	return e, root

def print_bst(root):
	stack = []
	stack.append(((1, len(root) - 1), ' is root'))

	while stack:
		value = stack.pop()
		if type(value[0]) == str:
			print ''.join(value)
		else:
			left = value[0][0]
			right = value[0][1]
			rootval = root[left][right]
			print 'p%d%s' % (rootval , value[1])

			if rootval == left:
				leftval = 'q%d' % (rootval - 1)
			else:
				leftval = (left, rootval - 1)

			if rootval == right:
				rightval = 'q%d' % rootval
			else:
				rightval = (rootval + 1, right)
				
			stack.append((rightval, ' is right of p%d' % rootval))
			stack.append((leftval, ' is left of p%d' % rootval))

			
			
		
	pass
		

	

if __name__ == '__main__':
	p = [0, 0.04, 0.06, 0.08, 0.02, 0.1, 0.12, 0.14]
	q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]

	e, root = optimal_bst(p, q)

	print e[1][len(p) - 1]
	print_bst(root)


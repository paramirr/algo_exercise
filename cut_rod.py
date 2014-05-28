#!/usr/local/bin/python2.7
import sys
import random
import time

def cut_rod(price, length):
	if length == 0:
		return 0
	result = -1

	for i in range(1, length + 1):
		result = max(result, price[i - 1] + cut_rod(price, length -i))
	return result

def memoize_cut_rod(price, revenue, length):
	if revenue[length] != -1:
		return revenue[length]

	result = -1

	for i in range(1, length + 1):
		result = max(result, price[i - 1] + memoize_cut_rod(price, revenue, length - i))
	
	revenue[length] = result
	return result
	
def bottom_up_cut_rod(price, length):
	revenue = [0] * (length + 1)
	
	for j in range(1, length + 1):
		result = -1
		for i in range(1, j + 1):
			result = max(result, price[i - 1] + revenue[j - i])
		revenue[j] = result
	
	return revenue[length]

def extended_bottom_up_cut_rod(price, length):
	revenue = [0] * (length + 1)
	size = [0] * (length + 1)

	for j in range(1, length + 1):
		result = -1
		for i in range(1, j + 1):
			if result < price[i - 1] + revenue[j - i]:
				result = price[i - 1] + revenue[j - i]
				size[j] = i
		revenue[j] = result
	
	return revenue, size
	

if __name__ == '__main__':
	length = int(sys.argv[1])
	price = [1]
	revenue = [0] + [-1] * length

	random.seed()
	for i in range(1, length):
		price.append(price[i-1] + random.randrange(5))
		
		
	#print price

	#start = time.clock()
	#print 'max profit of length %d is %d' % (length, cut_rod(price, length))
	#end = time.clock()
	#print 'normal cut rod time is %f' % (end - start)
	#start = time.clock()
	#print 'max profit of length %d is %d' % (length, memoize_cut_rod(price, revenue, length))
	#end = time.clock()
	#print 'memoized cut rod time is %f' % (end - start)
	start = time.clock()
	print 'max profit of length %d is %d' % (length, bottom_up_cut_rod(price, length))
	end = time.clock()
	print 'bottom up cut rod time is %f' % (end - start)

	start = time.clock()
	r, s = extended_bottom_up_cut_rod(price, length)
	print 'max profit of length %d is %d' % (length, r[length])
	print 'size of piece is ',
	while length > 0:
		print s[length],
		length -= s[length]
	end = time.clock()
	print 'bottom up cut rod time is %f' % (end - start)

#!/usr/local/bin/python2.7
#encoding:utf-8

cache = []

def dynamic_recursive_activity_select(acts, i, j):
    if cache[i, j] != -1:
        return cache[i, j]
    
    if i > j:
        return 0

    max = 9999

    for ind in range(i, j + 1):
        val = dynamic_recursive_activity_select(acts, 

def dynamic_iterative_activity_select(acts):
    pass


if __name__ == '__main__':
    acts = [ (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16), ]

    cache = [[-1 for i in range(len(acts))] for i in range(len(acts))]



#!/usr/bin/python3

import itertools

lists = [[1,2,3],[2,3,4]]

flatten_list = list(itertools.chain.from_iterable(lists))

print(flatten_list)


# $ ./8b-flatten-list.py 
# [1, 2, 3, 2, 3, 4]
#!/usr/bin/python3

list = [[1,2,3],[2,3,4]]

lists = [ i for j in list for i in j ]

# print(set(lists))
print(lists)


# $ ./8c-flatten-list.py 
# [1, 2, 3, 2, 3, 4]
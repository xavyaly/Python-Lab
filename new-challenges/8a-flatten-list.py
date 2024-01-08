#!/usr/bin/python3

list = [[1,2,3],[2,3,4]]

lists = []
for i in list:
    for j in i:
        lists.append(j)

# print(set(lists))
print(lists)


# $ ./8a-flatten-list.py 
# [1, 2, 3, 2, 3, 4]
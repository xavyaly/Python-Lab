#!/usr/bin/python3

a = [1,2,3,4,5,6,7,8,9,10]

# print(max(a))

max_no = max(enumerate(a, start=0), key = lambda a:a[1])
# min_no = min(enumerate(a, start=0), key = lambda a:a[1])

print("The index of maximum no is: ",  max_no[0])
# print("The index of minimum no is: ",  min_no[0])

# $ ./9a-largest.py 
# The index of maximum no is:  9
# Write a Python program to find the common elements between two lists.

def find_common_elements(lst1,lst2):
    return list(set(lst1) & set(lst2))

# print(find_common_elements((1,2,3),(2,3,4)))
# python3 10-common.py 
# [2, 3]

lst1 = input("Enter lst1 of elements: ").split()
lst1 = [int(num) for num in lst1]

lst2 = input("Enter lst2 of elements: ").split()
lst2 = [int(num) for num in lst2]

print(find_common_elements(lst1,lst2))

# Execution Output 

# python3 10-common.py 
# Enter lst1 of elements: 1 2 3
# Enter lst2 of elements: 2 3 4
# [2, 3]

# python3 10-common.py 
# Enter lst1 of elements: 12 23 34
# Enter lst2 of elements: 45 56 78
# []

# python3 10-common.py 
# Enter lst1 of elements: 1 23 45 5 
# Enter lst2 of elements: 1 24 46 56
# [1]


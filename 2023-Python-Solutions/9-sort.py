# Write a Python program to sort a list of tuples based on the second element of each tuple.

def sort_list_of_tuples(lst):
    lst.sort(key=lambda x:x[1])
    return lst 

lst = [('kolkata', 900), ('bangalore', 1200), ('bihar', 600), ('bengal', 1100)]

print (sort_list_of_tuples(lst))

# Execution Output 

# python3 9-sort.py 
# [('bihar', 600), ('kolkata', 900), ('bengal', 1100), ('bangalore', 1200)]

# Write a Python function to find the maximum and minimum elements in a list.

def find_max_min(lst):
    return max(lst), min(lst)

# lst = input("Enter a list of elements: ")
# print (find_max_min(lst))

input_list = input("Enter a list of numbers separated by spaces: ").split()
input_list = [int(num) for num in input_list]

result = find_max_min(input_list)
print("Max and Min of list is: ", result)

# Execution Output 

# python3 8-max-min.py 
# Enter a list of numbers separated by spaces: 1 2 3 4 5
# Max and Min of list is: (5, 1)

# python3 8-max-min.py 
# Enter a list of numbers separated by spaces: 1 2 3 4 6 7 10 
# Max and Min of list is: (10, 1)

# python3 8-max-min.py 
# Enter a list of numbers separated by spaces: 123 234 345 456 567 678 789
# Max and Min of list is: (789, 123)



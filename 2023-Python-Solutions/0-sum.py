# Write a Python program to calculate the sum of all elements in a list.

def calculate_sum(elements):
    total_sum = 0
    for num in elements:
        total_sum += num
    return total_sum

# Input the list dynamically
input_list = input("Enter a list of numbers separated by spaces: ").split()
input_list = [int(num) for num in input_list]

result = calculate_sum(input_list)
print("The sum of all elements in the list is:", result)

# Program Execution

# python3 ./0-sum.py
# Enter a list of numbers separated by spaces: 1 2 3
# The sum of all elements in the list is: 6

# python3 ./0-sum.py
# Enter a list of numbers separated by spaces: 10 20 30 1000
# The sum of all elements in the list is: 1060
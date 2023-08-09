# Write a Python program to find the second largest element in a list.

# def second_largest(lst):
#     if len(lst) < 2:
#         return None 
#     lst.sort()
#     return lst[-2]

# input_list = input("Enter list of nos: ").split()
# input_list = [num for num in input_list]

# result = second_largest(input_list)
# print(second_largest(result))

def find_second_largest(nums):
    if len(nums) < 2:
        return "List must have at least two elements."
    
    # Sort the list in descending order
    sorted_nums = sorted(nums, reverse=True)
    
    # Return the element at index 1 (the second largest element)
    return sorted_nums[1]

# Test the function
if __name__ == "__main__":
    input_list = [10, 4, 8, 2, 5, 9]
    result = find_second_largest(input_list)
    print("Second largest element:", result)


# Execution Output

# python3 11-second-largest.py 
# Second largest element: 9
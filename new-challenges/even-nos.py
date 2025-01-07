# Method 1

# #!/usr/bin/python3

# nos = [1, 7, 10, 3, 100, 50, 37, 46]
# new_list = []

# for i in nos:
#     if i % 2 == 0:
#         #print('Even nos: ', i)
#         new_list.append(i)
        
# print(new_list)


# Method 2 

# #!/usr/bin/python3

# nos = [1, 7, 10, 3, 100, 50, 37, 46]

# new_list = [i for i in nos if i%2==0]
# print(new_list)


# Method 3

# def find_even_numbers(numbers):
#     if not numbers:
#         return []
#     else:
#         if numbers[0]%2 == 0:
#             return [numbers[0]] + find_even_numbers(numbers[1:])
#         else:
#             return find_even_numbers(numbers[1:])
        
# nos = [1, 7, 10, 3, 100, 50, 37, 46]

# even_numbers = find_even_numbers(nos)
# print("Even numbers: ", even_numbers)
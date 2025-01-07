# Scenario 1

numbers = [1,3,4,6,9]
#srt_nums = sorted(numbers)
print("srt_nums: ", sorted(numbers))


# Scenario 2

# Sorting in descending order

# numbers = [1,10,4,0,9]
# #srt_nums = sorted(numbers)
# print("srt_nums: ", sorted(numbers,reverse=True))


# Scenario 3:

# string = ["Ali", "Monkey", "Bob", "Chee"]
# print("Sorted Names: ", sorted(string))


# Scenario 4:

# tuple_data = (5, 3, 8, 1, 9)
# sorted_tuple = sorted(tuple_data)
# print("Sorted Tuple (as List):", sorted_tuple)


# Scenario 5:

# string = ["Ali", "Mo", "Bob", "Chee"]
# print("Sorted Names: ", sorted(string,key=len))


# Scenario 6:

# Sorting by items 

# data = {"c": 2, "a": 1, "d": 10, "b": 3}
# print("Sorted data: ", sorted(data))


# Scenario 7:

# Sorting by values

# data = {"c": 2, "a": 1, "d": 10, "b": 3}
# print("Sorted data: ", sorted(data.items(), key=lambda x: x[1]))


# Scenario 8:

# Sorting with case-sensitive

# names = ["john", "Alice", "bob", "David"]
# print("Sorted data: ", sorted(names, key=str.lower))


# Scenario 9:

# nested_list = [[1, 3], [3, 2], [2, 5], [4, 1]]
# # Sort by the second element of each sublist
# sorted_nested = sorted(nested_list, key=lambda x: x[1])
# print("Sorted Nested List:", sorted_nested)
# Write a Python function to remove duplicates from a list.

def remove_duplicates(string):
    return list(set(string))

str = input("Enter a string: ")
print(remove_duplicates(str))

# Execution Output

# python3 6-duplicates.py 
# Enter a string: abcc
# ['a', 'c', 'b']

# python3 6-duplicates.py 
# Enter a string: hhhhhhjjjjjkkkk
# ['j', 'k', 'h']

# python3 6-duplicates.py 
# Enter a string: malayalam
# ['m', 'y', 'l', 'a']
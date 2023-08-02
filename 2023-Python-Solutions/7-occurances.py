# Write a Python program to count the occurrences of each element in a list.

def count_occurances(lst):
    from collections import Counter
    return Counter(lst)

str = input("Enter a string: ")
print (count_occurances(str))

# Execution Output

# python3 7-occurances.py 
# Enter a string: aabbcc
# Counter({'a': 2, 'b': 2, 'c': 2})

# python3 7-occurances.py 
# Enter a string: fghjtyudfghjertyucvbnmdfghj
# Counter({'f': 3, 'g': 3, 'h': 3, 'j': 3, 't': 2, 'y': 2, 'u': 2, 'd': 2, 'e': 1, 'r': 1, 'c': 1, 'v': 1, 'b': 1, 'n': 1, 'm': 1})

# python3 7-occurances.py 
# Enter a string: 112233aabbccdd
# Counter({'1': 2, '2': 2, '3': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2})
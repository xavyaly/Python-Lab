# Print the words in a sentence in reversed order. For example write the code ‘John loves Python’such that we get ‘Python loves John’

# Method 1

String = "John loves Python"
# rev = list(reversed(String.split()))
# print(rev)

# Method 2

# String = "John loves Python"
# rev_string = (" ".join(String.split()[::-1]))
# print("Rev string: ", rev_string)

# Method 3

# String = "John loves Python"
# print(list(reversed(String.split())))

# Method 4

rev = (" ".join(String.split()[::-1]))
print(rev)

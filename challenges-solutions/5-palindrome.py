# Write a Python function to check if a given word is a palindrome.

def is_palindrome(word):
    return word == word[::-1]

str = input("Enter a string: ")
print(is_palindrome(str))

# Execution Output

# python3 5-palindrome.py 
# Enter a string: abba
# True

# python3 5-palindrome.py 
# Enter a string: abcd
# False

# python3 5-palindrome.py 
# Enter a string: malayalam           
# True
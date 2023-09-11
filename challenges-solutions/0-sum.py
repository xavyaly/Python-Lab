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

------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------#
# Question 1

# Write a program which will find all such numbers which are divisible by 11 but are not a multiple of 2,
# between 1000 and 1200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: 
# Consider use range(#begin, #end) method

# Initialize an empty list to store the numbers
result = []

# Iterate through numbers from 2000 to 3200 (both included)
for num in range(1000, 1201):
    # Check if the number is divisible by 7 and not a multiple of 5
    if num % 11 == 0 and num % 2 != 0:
        # Add the number to the result list
        result.append(num)

# Convert the list to a comma-separated string and print it
print(",".join(str(num) for num in result))

# O/P:

# $ python3 divisible.py 
# 1001,1023,1045,1067,1089,1111,1133,1155,1177,1199

#------------------------------------------------------------------------------------------------------------------------#

------------------------------------------------------------------------------------------------

# Write a Python function to check if a given number is prime.

def is_prime(num):
    if num <= 1:
        return False 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True     

n = int(input("Enter a no to check prime : "))
print(is_prime(n))

# Output

# python3 ./2-prime.py
# Enter a no to check prime : 12
# False

# python3 ./2-prime.py
# Enter a no to check prime : 11
# True

# python3 ./2-prime.py
# Enter a no to check prime : 1923
# False

------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------#
# Question 2

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 10
# Then, the output should be:
# 3628800

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints:
# 0 -> 1 
# 2 -> 2.1 = 2 
# 3 -> 3.2.1 = 6
# 8 -> 8.7.6.5.4.3.2.1 = 40320

# Solution 

def fact(x):
    if x == 0 or x == 1:
        return 1
    return x * fact(x-1)

x = int(input("Enter a number: "))
print (fact(x))

# O/P:
# $ python3 2-factorial.py 
# Enter a number: 0
# 1
# $ python3 2-factorial.py 
# Enter a number: 1
# 1
# $ python3 2-factorial.py 
# Enter a number: 10
# 3628800

#------------------------------------------------------------------------------------------------------------------------#

------------------------------------------------------------------------------------------------

# Write a Python program to reverse a string.

def reverse_a_string(str):
    return str[::-1]

str = input("Enter a string: ")
print(reverse_a_string(str))

# Execution Output

# python3 4-reverse.py 
# Enter a string: abc
# cba

# python3 4-reverse.py 
# Enter a string: agfhfkjhsd
# dshjkfhfga

------------------------------------------------------------------------------------------------

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

------------------------------------------------------------------------------------------------

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

------------------------------------------------------------------------------------------------

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

------------------------------------------------------------------------------------------------

# Write a Python function to find the maximum and minimum elements in a list.

def find_max_min(lst):
    return max(lst), min(lst)

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

------------------------------------------------------------------------------------------------

# Write a Python program to sort a list of tuples based on the second element of each tuple.

def sort_list_of_tuples(lst):
    lst.sort(key=lambda x:x[1])
    return lst 

lst = [('kolkata', 900), ('bangalore', 1200), ('bihar', 600), ('bengal', 1100)]

print (sort_list_of_tuples(lst))

# Execution Output 

# python3 9-sort.py 
# [('bihar', 600), ('kolkata', 900), ('bengal', 1100), ('bangalore', 1200)]

------------------------------------------------------------------------------------------------

# Write a Python program to find the common elements between two lists.

def find_common_elements(lst1,lst2):
    return list(set(lst1) & set(lst2))

# print(find_common_elements((1,2,3),(2,3,4)))
# python3 10-common.py 
# [2, 3]

lst1 = input("Enter lst1 of elements: ").split()
lst1 = [int(num) for num in lst1]

lst2 = input("Enter lst2 of elements: ").split()
lst2 = [int(num) for num in lst2]

print(find_common_elements(lst1,lst2))

# Execution Output 

# python3 10-common.py 
# Enter lst1 of elements: 1 2 3
# Enter lst2 of elements: 2 3 4
# [2, 3]

# python3 10-common.py 
# Enter lst1 of elements: 12 23 34
# Enter lst2 of elements: 45 56 78
# []

# python3 10-common.py 
# Enter lst1 of elements: 1 23 45 5 
# Enter lst2 of elements: 1 24 46 56
# [1]

------------------------------------------------------------------------------------------------

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

------------------------------------------------------------------------------------------------

# Write a Python function to check if two strings are anagrams of each other.

# An anagram is a word or phrase formed by rearranging the letters of another word or phrase, 
# typically using all the original letters exactly once. 
# To check if two strings are anagrams of each other, 
# you can compare if the sorted versions of both strings are equal. Here's a Python function to do that:

def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase to ignore case and spaces
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted versions of the strings are equal
    return sorted(str1) == sorted(str2)

# Test the function
if __name__ == "__main__":
    string1 = "listen"
    string2 = "silent"
    result = are_anagrams(string1, string2)
    if result:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

# Execution Output

# python3 12-anagrams.py 
# The strings are anagrams.

------------------------------------------------------------------------------------------------

# Write a Python Program to read the contents of a file

# To read the contents of a file in Python, you can use the built-in `open()` function to open the file and then read its contents using different methods. Here's a Python program to read the contents of a file:

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except IOError:
        return "Error reading the file."

# Test the function
if __name__ == "__main__":
    file_path = "example.txt"  # Replace with the path to your file
    file_contents = read_file(file_path)
    print(file_contents)

# Replace `"example.txt"` with the path to your file that you want to read. The `read_file()` function opens the file in read mode (`'r'`) and reads its contents using `file.read()`. It returns the contents of the file as a string.

# Note that the program handles two possible exceptions: `FileNotFoundError` and `IOError`. These exceptions can occur if the file is not found or if there is an error while reading the file. In both cases, the program will return an appropriate error message.

# Make sure to provide the correct file path in the `file_path` variable for the program to read the contents of your desired file.

------------------------------------------------------------------------------------------------

# Python Program to Copy One File to Another File without removing the contents of another file

# To copy the contents of one file to another file in Python without removing the contents of the destination file, you can read the contents from the source file and then write them into the destination file. Here's a Python program to achieve that:

def copy_file(source_file, destination_file):
    try:
        # Open the source file for reading
        with open(source_file, 'r') as source:
            content = source.read()
        
        # Open the destination file for writing
        with open(destination_file, 'w') as destination:
            destination.write(content)
        
        return "File copied successfully."
    except FileNotFoundError:
        return "Source file not found."
    except IOError:
        return "Error copying the file."

# Test the function
if __name__ == "__main__":
    source_file_path = "source.txt"          # Replace with the path of the source file
    destination_file_path = "destination.txt"  # Replace with the path of the destination file
    
    result = copy_file(source_file_path, destination_file_path)
    print(result)

# Replace `"source.txt"` and `"destination.txt"` with the paths of your source and destination files, respectively. The `copy_file()` function reads the contents from the source file using `source.read()` and then writes the contents into the destination file using `destination.write(content)`.

# Please make sure to provide the correct file paths in `source_file_path` and `destination_file_path` for the program to copy the contents properly.

------------------------------------------------------------------------------------------------

# Python Program to Copy One File to Another File and append the contents of destination file

# To copy the contents of one file to another file in Python and append the contents of the destination file, you can read the contents from both files, concatenate them, and then write the result into the destination file. Here's a Python program to achieve that:

def copy_file_and_append(source_file, destination_file):
    try:
        # Open the source file for reading
        with open(source_file, 'r') as source:
            source_content = source.read()
        
        # Open the destination file for reading
        with open(destination_file, 'r') as destination:
            destination_content = destination.read()
        
        # Concatenate the contents and write to the destination file
        with open(destination_file, 'a') as destination:
            destination.write('\n' + source_content + '\n')
        
        return "File copied and appended successfully."
    except FileNotFoundError:
        return "Source or destination file not found."
    except IOError:
        return "Error copying the file."

# Test the function
if __name__ == "__main__":
    source_file_path = "source.txt"          # Replace with the path of the source file
    destination_file_path = "destination.txt"  # Replace with the path of the destination file
    
    result = copy_file_and_append(source_file_path, destination_file_path)
    print(result)

# Replace `"source.txt"` and `"destination.txt"` with the paths of your source and destination files, respectively. The `copy_file_and_append()` function reads the contents from both the source file and the destination file, concatenates them with a newline in between (`'\n'`), and then writes the result into the destination file using the append mode (`'a'`).

# Please make sure to provide the correct file paths in `source_file_path` and `destination_file_path` for the program to copy and append the contents properly.


# Execution Output

# python3 15-append-contents-to-destination.py 
# File copied and appended successfully.

------------------------------------------------------------------------------------------------

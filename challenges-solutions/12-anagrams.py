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

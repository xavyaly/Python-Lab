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
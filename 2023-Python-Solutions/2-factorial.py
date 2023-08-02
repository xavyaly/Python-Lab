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

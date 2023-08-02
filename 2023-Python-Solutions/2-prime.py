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
#!/usr/bin/python3

a,b = 10,20

a ^= b 

b ^= a 

a ^= b 

print(f"a is {a}")
print(f"b is {b}")


# $ ./6b-swap-var.py 
# a is 20
# b is 10
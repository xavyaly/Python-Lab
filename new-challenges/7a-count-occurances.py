#!/usr/bin/python3

from collections import Counter

list = ["java","java","python"]

occurances = Counter(list).get("java")

print(f"The string appears " f"{occurances} times")


# $ ./7a-count-occurances.py 
# The string appears 2 times
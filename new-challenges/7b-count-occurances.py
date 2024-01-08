#!/usr/bin/python3

list = ["java","java","python"]

counter = 0
for i in list:
    if i == "java":
        counter+= 1

print(f"The string appears " f"{counter} times")


# $ ./7b-count-occurances.py 
# The string appears 2 times
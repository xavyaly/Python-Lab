#!/usr/bin/python

# IMPORT A MODULE
import os
import sys

# CREATE A RANDOM LIST
randomList = ['z',0,4]

# CODE
for i in randomList:
	try:
		print("The entry is: ", i)
		r = 1/int(i)
		break
	except:
		print("Oops", sys.exc_info()[0],"occured")
		print("Next Entry!!!")
print("The reciprocal of: ", i , "is", r)

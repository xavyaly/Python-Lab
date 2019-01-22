#!/usr/bin/python

# Initialize the function

def foo():
	print('Calling from inside the funtion!!!')
	return 2

if __name__ == '__main__':
	print("Going to call foo function...")
	i = foo()
	print("Called foo function ..")
	print('foo returned: '+str(i))



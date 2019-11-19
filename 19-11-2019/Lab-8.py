// FUNCTION:

$ cat Lab-8.py 
#!/usr/bin/python

#initialize a function

def foo():
	print('Calling from inside the function!!!')
	return 2

#calling function
if __name__ == '__main__':
	print('Going to call a foo function...')
	i=foo()
	print('Called foo function..')
	print('foo returned: '+str(i))

O/P:

$ chmod +x Lab-8.py
$ ./Lab-8.py 
Going to call a foo function...
Calling from inside the function!!!
Called foo function..
foo returned: 2


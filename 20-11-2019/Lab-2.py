Functions: 
	doc_string

Syntax:

def function_name(parameters):
	“function_docstring”
		function_suite
	return [expression]

$ cat Lab-2.py 
#!/usr/bin/python

#Initialize a function

def function_name(str):
	"This prints a passed string into this function!!!"
	
	print(str)
	return;

#Calling function

function_name("I'm the one who met with you !!!")
function_name("Again i am calling the same function!!!")
	
O/P:

$ chmod +x Lab-2.py
$ ./Lab-2.py 
I'm the one who met with you !!!
Again i am calling the same function!!!

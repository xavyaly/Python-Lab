Looping: 
	while:: Executes a target statements as long as a given condition is true

Syntax:
	WHILE EXPRESSION:
		STATEMENTS(S)

$ cat Lab-1.py 
#!/usr/bin/python

count=0
while(count<9):
	print("The count will be: ",count)
	count=count+1

print("Leave it!!!")

O/P:

$ chmod +x Lab-1.py
$ ./Lab-1.py 
('The count will be: ', 0)
('The count will be: ', 1)
('The count will be: ', 2)
('The count will be: ', 3)
('The count will be: ', 4)
('The count will be: ', 5)
('The count will be: ', 6)
('The count will be: ', 7)
('The count will be: ', 8)
Leave it!!!


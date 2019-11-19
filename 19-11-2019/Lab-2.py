// INFINITE LOOP

$ cat Lab-2.py 
#!/usr/bin/python

count=1
while count==1:
	a=input("Enter any no: ")
	print("You have entered: ", a)

print("Leave it!!!")

O/P: Press CTRL+C to interrupt the execution forcefully

$ ./Lab-2.py 
Enter any no: 12
('You have entered: ', 12)
Enter any no: 10
('You have entered: ', 10)
Enter any no: 0
('You have entered: ', 0)
Enter any no: 13
('You have entered: ', 13)
Enter any no: ^CTraceback (most recent call last):
  File "./Lab-2.py", line 5, in <module>
    a=input("Enter any no: ")
KeyboardInterrupt

Loop control: 
	assert

$ cat Lab-1.py 
#!/usr/bin/python

i=int(input('Enter any no smaller than 10..'))
assert i<10, 'Entered by user is wrong!!! Please type different no...'

print('Entered by user is: ', i)

O/P:

$ chmod +x Lab-1.py
$ ./Lab-1.py 
Enter any no smaller than 10..^X^CTraceback (most recent call last):
  File "./Lab-1.py", line 3, in <module>
    i=int(input('Enter any no smaller than 10..'))
KeyboardInterrupt

$ ./Lab-1.py 
Enter any no smaller than 10..: 9
('Entered by user is: ', 9)

$ ./Lab-1.py 
Enter any no smaller than 10..: 11
Traceback (most recent call last):
  File "./Lab-1.py", line 4, in <module>
    assert i<10, 'Entered by user is wrong!!! Please type different no...'
AssertionError: Entered by user is wrong!!! Please type different no...

$ ./Lab-1.py 
Enter any no smaller than 10..: 10.2
Traceback (most recent call last):
  File "./Lab-1.py", line 4, in <module>
    assert i<10, 'Entered by user is wrong!!! Please type different no...'
AssertionError: Entered by user is wrong!!! Please type different no...

$ ./Lab-1.py 
Enter any no smaller than 10..: 2.3
('Entered by user is: ', 2)

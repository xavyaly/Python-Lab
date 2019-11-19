// INFINITE LOOP IN WHILE:

$ cat Lab-4.py 
#!/usr/bin/python

flag=1
while(flag):
	print('Given flag is True!!!')

print('Leave it!!!')

O/P:

Given flag is True!!!
Given flag is True!!!
Given flag is True!!!
Given flag is True!!!
Given flag is True!!!
Given flag is True!!!
Given flag is True!!!
Given flag is True!!!
Given flag is True!!!
Traceback (most recent call last):
  File "./Lab-4.py", line 5, in <module>
    print('Given flag is True!!!')
KeyboardInterrupt

// IT KEEPS ON ITERATING UNLESS AND UNTILL WE PRESS CTRL+C



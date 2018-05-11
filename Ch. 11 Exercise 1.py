#Exercise 1: Write a simple program to simulate the operation of the grep command
#on Unix. Ask the user to enter a regular expression and count the number
#of lines that matched the regular expression:

import re
x = input("Enter a regular expression: ")
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
        line = line.rstrip()
        if re.search(x, line):
                count = count +1
                #print(line)
print ('The file had ',count, 'lines that matched',x)
                


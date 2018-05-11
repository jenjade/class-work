#Exercise 2: Write a program to look for lines of the form
#`New Revision: 39772`
#and extract the number from each of the lines using a regular expression and
#the findall() method. Compute the average of the numbers and print out the
#average.

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
                


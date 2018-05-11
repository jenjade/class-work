#Exercise 2: Write a program that categorizes each mail message by which day of
#the week the commit was done. To do this look for lines that start with “From”,
#then look for the third word and keep a running count of each of the days of the
#week. At the end of the program print out the contents of your dictionary (order
#does not matter).


fhand = open('mbox-short.txt')
count = 0
counts = dict()
for line in fhand:
    if line.startswith('From'):
        line = line.split()
        if len(line) > 2:
            day = line[2]
            for day in line:
                if day not in counts:
                    counts[day] = 1
                else:
                    counts[day] = counts[day] + 2
print (counts)

input ("Press enter to continue")            

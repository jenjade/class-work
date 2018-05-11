#Write a program to read through a mail log, build a histogram using
#a dictionary to count how many messages have come from each email address, and
#print the dictionary.

fhand = open('mbox-short.txt')
count = 0
counts = dict()
for line in fhand:
    if line.startswith('From'):
        line = line.split()
        if len(line) > 2:
            day = line[1]
            domain = day.split("@")[1]
            counts = dict()
            print (domain)
            for domain in line:
                counts[domain] = counts.get(domain,0)+1
print (counts)
input ("Press enter to continue")

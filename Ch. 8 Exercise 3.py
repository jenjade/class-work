fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) > 2 and words[0] == 'From': 
        print(words[2])

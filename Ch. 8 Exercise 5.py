fhand = open('mbox-short.txt')
count = 0
search_word = 'From'
for line in fhand:
    dict()
    words = line.split()
    #print ('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])
    count += 1
    
print ('The word From occurs', count, 'times.')
    


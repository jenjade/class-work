fhand = open ('mbox-short.txt')
x = dict()
for line in fhand:
    if line.startswith('From:'):
        line = line.split()
        email = line[1]
        x[email] = x.get(email,0)+1
        
for word in email:
    if word not in x:
        x[word] = 1
    else:
        x[word] += 1
print (x)
input ("Press enter to continue")    

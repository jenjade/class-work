romeo_sort = open('romeo.txt')
numlist = list()
for line in romeo_sort:
    line = line.rstrip()
    words = line.split()
    for x in words:
        if x not in numlist:
            numlist.append(x)
numlist.sort()
print (numlist)

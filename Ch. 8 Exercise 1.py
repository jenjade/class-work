##Part 1

x = ['Iron Man', 'Spiderman', 'Thor', 'Black Widow']
def chop(x):
    del x[0]
    del x[-1]
print ('Part 1 - Original list:',x)
y = chop (x)
print ('Part 1 - Chopped list:',x)
print (y)

##Part 2

x1 = ['Dr. Strange', 'Loki', 'Captain America', 'Hulk']
def middle(x1):
    del x1[0]
    del x1[-1]
print ('Part 2 - Original list:',x1)
a = middle (x1)
print ('Part 2 - Middle list:',x1)


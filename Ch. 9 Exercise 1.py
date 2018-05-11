#Write a program that reads the words in words.txt and stores them as keys in
#a dictionary. It doesn’t matter what the values are. Then you can use the in
#operator as a fast way to check whether a string is in the dictionary.

x = open ('words.txt')
y = dict()
z = x.read().split()
print(z)
x1 = 'are' in z
print ("'are' in z")
print (x1)

input ("Press enter to continue")

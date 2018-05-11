result = []

for a in range(1,8):
    number = int(input("Enter a number ('done' when finished): "))
    result.append(number)
print (result)
print ('The highest vaule number is ',max(result))
print ('The lowest vaule number is ', min(result))

def listsum(listf):
    sum = 0
    for i in range (len(listf)):
        sum = sum + listf[i]
    return sum
def liststring(listf):
    stringsum = " " + str(listf[0])
    for i in range (1,len(listf)):
        stringsum = stringsum + ", " + str(listf[i])
    return stringsum
list1 = []
print("Enter numbers:")
while True:
    temp = input()
    if (temp.lower() != "end"):
        list1.append(int(temp))
    else:
        break
print("You entered" + liststring(list1))
print("Total: %i"%(listsum(list1)))

average = listsum(list1)/len(list1)
print("Average: %.2f" %(average))
    
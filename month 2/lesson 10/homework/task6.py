print("Enter grade for Jake:")
jake = float(input())
print("Enter grade for John:")
john = float(input())
print("Enter grade for Jack:")
jack = float(input())
print("Enter grade for Jane:")
jane = float(input())
meangrade = (jake + john + jane + jack)/4
if (meangrade*10-int(meangrade)*10 >= 5): 
    meangrade = int(meangrade) + 1
else:
    meangrade = int(meangrade)
print("The mean grade of all 4 students is:")
print(meangrade)





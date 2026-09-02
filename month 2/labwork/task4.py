import random

group_0=[]
group_10=[]
group_20=[]
group_30=[]
group_40=[]
group_50=[]
group_60=[]
group_70=[]
group_80=[]
group_90=[]
print("Введите количество тестов:")
total_tests = int(input())

for i in range (0,total_tests):
    temp =  random.randint(0,99)
    if temp >= 90:
        group_90.append(temp)
    elif temp >= 80 and temp < 90:
        group_80.append(temp)
    elif temp >= 70 and temp < 80:
        group_70.append(temp)
    elif temp >= 60 and temp < 70:
        group_60.append(temp)
    elif temp >= 50 and temp < 60:
        group_50.append(temp)
    elif temp >= 40 and temp < 50:
        group_40.append(temp)  
    elif temp >= 30 and temp < 40:
        group_30.append(temp)
    elif temp >= 20 and temp < 30:
        group_20.append(temp)
    elif temp >= 10 and temp < 20:
        group_10.append(temp)
    elif temp >= 0 and temp < 10:
        group_0.append(temp)      
print("Total number of samples:", end="")
print(total_tests)
print("Group 0-9:", end="")
print(len(group_0))
print("Group 10-19:", end="")
print(len(group_10))
print("Group 20-29:", end="")
print(len(group_20))
print("Group 30-39:", end="")
print(len(group_30))
print("Group 40-49:", end="")
print(len(group_40))
print("Group 50-59:", end="")
print(len(group_50))
print("Group 60-69:", end="")
print(len(group_60))
print("Group 70-79:", end="")
print(len(group_70))
print("Group 80-89:", end="")
print(len(group_80))
print("Group 90-99:", end="")
print(len(group_90))
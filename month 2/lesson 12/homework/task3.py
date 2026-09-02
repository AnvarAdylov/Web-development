def compare(n,listtocomp):
    print("Result:")
    for i in range (len(listtocomp)):
        print("%i) %i > %i == %r" %( i+1 , listtocomp[n], listtocomp[i], listtocomp[n]>listtocomp[i] ))
list = []
print("Enter numeric value for first element:")
list.append(int(input()))
print("Enter numeric value for second element:")
list.append(int(input()))
print("Enter numeric value for third element:")
list.append(int(input()))
print("Enter key of element for comparison: in range from 0 to %i" %(len(list)))
a = int(input())
compare(a,list)


def multab(n):
    print("multiplication table for number %i:" %(n))
    for i in range (9):
        print("%i X %i == %i" %(n,i+1, n*(i+1) ))

print("Input which numbers multiplication table you want to receive:")
a = int(input())
multab(a)

print("Full table implementation:")
for i in range(10):
    multab(i)
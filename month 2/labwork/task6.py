import array as arr
import random as rnd
def max_in_array(array):
    max = array[0]
    for i in range (len(array)):
        if max < array[i]:
            max = array[i]
    return max
array_a = []
array_b = []
array_c = []

for i in range (10):
    array_a.append(rnd.randint(1,100))
    array_b.append(rnd.randint(1,100))

for i in range (10):
    array_c.append(array_a[i] + array_b[i])
print("Массив A:", end="")  
print(array_a)

print("Массив B:", end="")
print(array_b)
print("Массив C:", end="")
print(array_c)
print("Max:", end="")
print(max_in_array(array_c))
def intersection(x, y):
    return list(set(x) & set(y))


first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


a = [1, 3, 6, 12]

b = [0, 1, 12, 4]

c = intersection(a, b)

print(c)

third = intersection(first, second)

print(third)

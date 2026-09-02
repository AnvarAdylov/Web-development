def sort_list(numbers, is_reversed):
    if is_reversed:
        if len(numbers) == 1:
            return numbers
        max = numbers[0]
        max_index = 0
        for i in range(len(numbers)):
            if (max < numbers[i]):
                max = numbers[i]
                max_index = i
        temp = numbers[0]
        numbers[0] = numbers[max_index]
        numbers[max_index] = temp
        numbers[1:len(numbers)] = sort_list(numbers[1:len(numbers)], True)
    else:
        if len(numbers) == 1:
            return numbers
        min = numbers[0]
        mindex = 0
        for i in range(len(numbers)):
            if (min > numbers[i]):
                min = numbers[i]
                mindex = i
        temp = numbers[0]
        numbers[0] = numbers[mindex]
        numbers[mindex] = temp
        numbers[1:len(numbers)] = sort_list(numbers[1:len(numbers)], False)
    return numbers


numbers = [4, -2, 5, 7, 0, 1]
sorted_list = sort_list(numbers, False)

print(sorted_list)
sorted_list = sort_list(numbers, True)
print(sorted_list)

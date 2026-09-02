nums = [45, 90, 44, 37, 95, 50, 220, 185, 210, 205, 25, 33]

nums_remainder = [[nums[i]] for i in range(0, len(nums)) if nums[i] % 15 == 0]

print(nums_remainder)

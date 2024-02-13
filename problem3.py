def find_max(numbers, compare):
    max_num = numbers[0]

    for num in numbers[1:]:
        max_num = compare(max_num, num)

    return max_num

numbers = [5, 12, 3, 8, 15, 1]
compare = lambda x, y: x if x > y else y

print(find_max(numbers, compare))

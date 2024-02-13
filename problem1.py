def sum_of_digits(num):
    digits = map(int, str(num))

    digits = filter(lambda x: x >= 0, digits) 

    return sum(digits)

number = 123
print(sum_of_digits(number))

list1 = [8, 57, 300, -3, 0]
list2 = [-3, 4, 57, 0, 7]

intersection = list(filter(lambda x: x in list2, list1))

print(intersection)

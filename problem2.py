strings = ["ia", "m", "ast", "ring"]

sorted_strings = sorted(strings, key=lambda x: (len(x), x))

print(sorted_strings)

dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
dict2 = {}

for key, val in dict.items():
    if val > 2:
        dict2[key] = val

print(dict2)
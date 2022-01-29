src, result = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11], []
#result = [23, 1, 3, 10, 4, 11]
for elem in src:
    if src.count(elem) == 1:
        result.append(elem)

print(result)
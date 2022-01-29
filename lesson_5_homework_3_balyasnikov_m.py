src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
result = []
for count, elem in enumerate(src):
    if count == 0:
        continue
    else:
        if elem > src[count-1]:
            result.append(src[count])

print(result)
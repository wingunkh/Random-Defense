a = []
result1 = 0
result2 = []

for i in range(1, 9):
    n = int(input())
    a.append((n, i))

a.sort(key = lambda x: x[0], reverse = True)

for i in range(5):
    score, number = a[i]
    result1 += score
    result2.append(number)

result2.sort()

print(result1)
print(*result2, sep = ' ')

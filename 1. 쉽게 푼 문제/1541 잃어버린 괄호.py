a = input().split('-')
result = 0

for i in a[0].split('+'):
    result += int(i)

for i in range(1, len(a)):
    tmp = a[i].split('+')

    for j in tmp:
        result -= int(j)
else:
    print(result)

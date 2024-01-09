a = input().split('-')
buff = a[0].split('+')
result = 0

for i in buff:
    result += int(i)

if len(a) == 1:
    print(result)
else:   
    for i in range(1, len(a)):
        buff = a[i].split('+')
        for j in buff:
            result -= int(j)

    print(result)

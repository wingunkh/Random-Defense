n, m = map(int, input().split())
a = [i for i in range(10000001)]
a[1] = 0
result = 0

for i in range(2, int(len(a) ** 0.5) + 1):
    if a[i] == 0:
        continue
    
    for j in range(i + i, len(a), i):
        a[j] = 0

for i in range(2, len(a)):
    if a[i] == 0:
        continue

    tmp = a[i] * a[i]

    while tmp <= m:
        if tmp >= n:
            result += 1

        tmp *= a[i]

print(result)

n = int(input())
a = list(map(int, input().split()))
target = 0

for i in range(n - 1, 0, -1):
    if a[i] > a[i - 1]:
        target = i - 1
        break

for j in range(n - 1, 0, -1):
    if a[target] < a[j]:
        a[target], a[j] = a[j], a[target]
        result = a[:target + 1] + sorted(a[target + 1:])
        print(' '.join(map(str, result)))
        break
else:
    print(-1)

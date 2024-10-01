t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    best = a[-1]
    result = 0

    for i in range(n - 2, -1, -1):
        if a[i] < best:
            result += best - a[i]
        elif a[i] > best:
            best = a[i]

    print(result)

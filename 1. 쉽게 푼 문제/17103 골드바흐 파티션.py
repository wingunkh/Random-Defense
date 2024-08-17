import sys
input = sys.stdin.readline

t = int(input())
a = [i for i in range(1000001)]
a[1] = 0

for i in range(2, int(1000000 ** 0.5) + 1):
    for j in range(i + i, 1000001, i):
        a[j] = 0

for _ in range(t):
    n = int(input())
    result = 0

    if a[2] + a[n - 2] == n:
        result += 1

    for i in range(3, n // 2 + 1, 2):
        if a[i] + a[n - i] == n:
            result += 1

    print(result)

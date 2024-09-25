import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
result = sys.maxsize

for _ in range(m):
    s, e, w = map(int, input().split())
    a[s][e] = min(a[s][e], w)

for k in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            a[s][e] = min(a[s][e], a[s][k] + a[k][e])

for s in range(1, n + 1):
    for e in range(1, n + 1):
        if s == e:
            result = min(result, a[s][e])

if result == sys.maxsize:
    print(-1)
else:
    print(result)

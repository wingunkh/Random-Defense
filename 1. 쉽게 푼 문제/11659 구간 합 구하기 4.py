import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0 for _ in range(n+1)]

for i in range(1, n+1):
    s[i] = s[i-1] + a[i-1]

for _ in range(m):
    start, end = map(int, input().split())

    print(s[end] - s[start-1])

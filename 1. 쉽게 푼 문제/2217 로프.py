import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
a.sort(reverse = True)
result = 0

for i in range(n):
    result = max(result, a[i] * (i + 1))

print(result)

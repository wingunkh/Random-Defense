import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
result = 0

for _ in range(n):
    s.add(input().rstrip())

for _ in range(m):
    if input().rstrip() in s:
        result += 1

print(result)

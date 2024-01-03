import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

a.sort(key = lambda x: x[0])
a.sort(key = lambda x: x[1])

for i in a:
    print(i[0], i[1])

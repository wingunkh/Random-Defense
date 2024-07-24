import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    name, x, y, z = input().rstrip().split()
    x, y, z = int(x), int(y), int(z)
    a.append((name, x, y, z))

a.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for name, _, _, _ in a:
    print(name)

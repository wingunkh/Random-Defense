import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [i for i in range(1, n + 1)]
i = 0
result = []

while a:
    i = (i + k - 1) % len(a)
    result.append(a.pop(i))

print("<" + ', '.join(map(str, result)) + ">")

import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
tmp = 0
start, end = 1, 1
result = sys.maxsize

for i in a:
    tmp = tmp + i
    s.append(tmp)

while end <= n:
    target = s[end] - s[start-1]

    if target >= m:
        result = min(result, end - start + 1)
        start += 1
    else:
        end += 1

if result == sys.maxsize:
    print(0)
else:
    print(result)

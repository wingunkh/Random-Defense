import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key = lambda x: x[0])
tmp = [a[0][0], a[0][1]]
result = 0

for i in range(1, n):
    s, e = a[i]

    if tmp[0] <= s and e <= tmp[1]:
        continue
    elif s < tmp[0] and tmp[1] < e:
        tmp = [s, e]
    elif s <= tmp[0] <= e:
        tmp[0] = s
    elif s <= tmp[1] <= e:
        tmp[1] = e
    else:
        result += tmp[1] - tmp[0]
        tmp = [s, e]
else:
    if tmp:
        result += tmp[1] - tmp[0]

print(result)

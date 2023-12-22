import sys
input = sys.stdin.readline

n = int(input())
a = sorted([int(input()) for _ in range(n)])
dic = {}
max_a = []

print(round(sum(a) / n))

print(a[n // 2])

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in dic:
    if dic[i] == max(dic.values()):
        max_a.append(i)

print(max_a[0]) if len(max_a) == 1 else print(max_a[1])

print(max(a) - min(a))

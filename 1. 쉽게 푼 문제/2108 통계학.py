import sys
input = sys.stdin.readline

n = int(input())
a = list(int(input()) for _ in range(n))
dic = {}
modes = []

print(round(sum(a) / n))

print(sorted(a)[n // 2])

for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in dic:
    if dic[i] == max(dic.values()):
        modes.append(i)

modes.sort()

if len(modes) == 1:
    print(modes[0])
else:
    print(modes[1])

print(max(a) - min(a))

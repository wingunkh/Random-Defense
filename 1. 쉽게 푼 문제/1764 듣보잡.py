import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = dict()
a = []

for _ in range(n + m):
    buff = input().rstrip()

    if buff in dic:
        dic[buff] += 1
    else:
        dic[buff] = 1

for i in dic:
    if dic[i] == 2:
        a.append(i)

a.sort()

print(len(a))
print(*a, sep = '\n')

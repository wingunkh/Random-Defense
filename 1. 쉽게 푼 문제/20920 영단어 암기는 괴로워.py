import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
dic = dict()
# key = 단어, value = 횟수

for _ in range(n):
    s = input().rstrip()

    if len(s) < m:
        continue

    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1

for i in dic:
    a.append((i, dic[i]))

a.sort(key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in a:
    print(i[0])

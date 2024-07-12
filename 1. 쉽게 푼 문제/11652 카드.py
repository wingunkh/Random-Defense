import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
result = []

for _ in range(n):
    tmp = int(input())

    if tmp not in dic:
        dic[tmp] = 1
    else:
        dic[tmp] += 1

maximum = max(dic.values())

for i in dic.keys():
    if dic[i] == maximum:
        result.append(i)

print(min(result))

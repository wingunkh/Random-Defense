import sys
input = sys.stdin.readline

n = int(input())
a = sorted([int(input()) for _ in range(n)])
dic = dict()
buff = []

print(round(sum(a) / n))

print(a[n // 2])

for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in dic:
    if dic[i] == max(dic.values()):
        buff.append(i)
else:
    buff.sort()
    
if len(buff) >= 2:
    print(buff[1])
else:
    print(buff[0])

print(max(a) - min(a))

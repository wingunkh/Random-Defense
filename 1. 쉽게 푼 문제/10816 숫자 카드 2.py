import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
dic = {}

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in b:
    if i in dic:
        print(dic[i], end = ' ')
    else:
        print(0, end = ' ')

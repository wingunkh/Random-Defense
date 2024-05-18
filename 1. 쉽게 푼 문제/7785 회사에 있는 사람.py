import sys
input = sys.stdin.readline

n = int(input())
dic = dict()

for _ in range(n):
    a, b = input().split()

    if a not in dic:
        dic[a] = 1
    else:
        del dic[a]

print(*sorted(dic.keys(), reverse = True), sep = "\n")

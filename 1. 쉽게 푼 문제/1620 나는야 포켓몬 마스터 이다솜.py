import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = dict()

for i in range(1, n+1):
    buff = input().rstrip()
    dic[str(i)] = buff
    dic[buff] = i

for _ in range(m):
    print(dic[input().rstrip()])

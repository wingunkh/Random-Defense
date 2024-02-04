import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = dict()

for _ in range(n):
    site, password = input().split()
    dic[site] = password

for _ in range(m):
    print(dic[input().rstrip()])

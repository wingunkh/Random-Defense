n = int(input())
dic = dict()

a = list(map(int, input().split()))
b = sorted(set(a))

for i in range(len(b)):
    dic[b[i]] = i 

for i in a:
    print(dic[i], end = ' ')

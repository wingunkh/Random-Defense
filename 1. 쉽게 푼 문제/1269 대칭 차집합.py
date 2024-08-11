n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dic = {}
result = 0

for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in b:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in dic:
    if dic[i] == 1:
        result += 1

print(result)

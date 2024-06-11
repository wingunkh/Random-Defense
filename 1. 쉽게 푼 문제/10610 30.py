a = list(map(int, input()))
a.sort(reverse = True)
a = int(''.join(map(str, a)))
dic = dict()

for i in str(a):
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

result = a - a % 30

for i in str(result):
    if i in dic:
        dic[i] -= 1

for i in dic:
    if dic[i] != 0:
        print(-1)
        break
else:
    print(result)

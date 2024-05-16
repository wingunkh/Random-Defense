a = list(map(int, input().replace('6', '9')))
dic = dict()

for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

if 9 in dic:
    if dic[9] % 2 != 0:
        dic[9] = dic[9] // 2 + 1
    else:
        dic[9] = dic[9] // 2

print(max(dic.values()))

n = int(input())
dic = dict()

for _ in range(n):
    s = input()

    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1

maximum = max(dic.values())

for i in sorted(dic.keys()):
    if dic[i] == maximum:
        print(i)
        break

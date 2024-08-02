n = int(input())
a = []
b = []
dic = dict()
result = 0

for _ in range(n):
    a.append(list(input()))

for word in a:
    for i in range(len(word)):
        if word[i] not in dic:
            dic[word[i]] = 10 ** (len(word) - i - 1)
        else:
            dic[word[i]] += 10 ** (len(word) - i - 1)

b = list(dic.values())
b.sort(reverse = True)

for i in range(len(b)):
    result += b[i] * (9 - i)

print(result)

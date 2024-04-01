n = int(input())
result = 0

for _ in range(n):
    s = input()
    dic = {}
    buff = ""

    for i in s:
        if i == buff:
            continue

        if i not in dic:
            dic[i] = True
            buff = i
        else:
            break
    else:
        result += 1

print(result)

n = int(input())
buff = list(map(int, input().split()))
a = [i for i in range(n + 1)]
fact = [1 for i in range(n + 1)]

for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i

if buff[0] == 1:
    target = buff[1]
    result = []

    for i in range(1, n + 1):
        tmp = 0
        
        while target - fact[n - i] > 0:
            target -= fact[n - i]
            tmp += 1

        for j in range(1, n + 1):
            if a[j] == -1:
                continue

            if tmp == 0:
                result.append(a[j])
                a[j] = -1
                break
            else:
                tmp -= 1

    print(*result)
else:
    target = buff
    result = 1

    for i in range(1, n + 1):
        count = 0

        for j in range(1, target[i]):
            if a[j] != -1:
                count += 1

        result += count * fact[n - i]
        a[target[i]] = -1

    print(result)

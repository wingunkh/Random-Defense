def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

t = int(input())

for _ in range(t):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    a = tmp[1:]
    result = 0

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            result += gcd(a[i], a[j])

    print(result)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = sorted([int(input()) for _ in range(n)])
interval = []
result = []

for i in range(n - 1):
    interval.append(a[i + 1] - a[i])

GCD = interval[0]

for i in range(1, len(interval)):
    GCD = gcd(GCD, interval[i])

for i in range(2, int(GCD ** 0.5) + 1):
    if GCD % i == 0:
        result.append(i)
        result.append(GCD // i)

result.append(GCD)
result = sorted(list(set(result))) 
print(*result)

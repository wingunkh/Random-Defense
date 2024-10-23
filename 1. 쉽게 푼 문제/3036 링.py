def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))
first = a[0]

for i in range(1, n):
    target = a[i]
    GCD = gcd(first, target) if first > target else gcd(target, first)
    print(f"{first // GCD}/{target // GCD}")

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

a, b = map(int, input().split())
c, d = map(int, input().split())

numerator = a * d + c * b
denominator = b * d
n = gcd(denominator, numerator)

print(numerator // n, denominator // n)

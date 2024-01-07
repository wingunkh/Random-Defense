def func(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (func(a, b // 2, c) ** 2) % c
    else:
        return ((func(a ,b // 2, c) ** 2) * a) % c

a, b, c = map(int, input().split())

print(func(a, b, c))

# 모듈로 연산 분배법칙
# (A + B) % N = ((A % N) + (B % N)) % N
# (A + B) % N = ((A % N) + (B % N)) % N
# (A - B) % N = ((A % N) - (B % N)) % N
# (A X B) % N = ((A % N) X (B % N)) % N

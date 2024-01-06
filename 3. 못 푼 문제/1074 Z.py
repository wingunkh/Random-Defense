def func(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n-1)

    # 좌상단 분면
    if r < half and c < half:
        return func(n-1, r, c)
    # 우상단 분면
    elif r < half and c >= half:
        return half * half + func(n-1, r, c - half)
    # 좌하단 분면
    elif r >= half and c < half:
        return 2 * half * half + func(n-1, r - half, c)
    # 우하단 분면
    else:
        return 3 * half * half + func(n-1, r - half, c - half)

n, r, c = map(int, input().split())
result = func(n, r, c)

print(result)

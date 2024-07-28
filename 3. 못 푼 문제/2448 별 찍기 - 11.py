def func(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]

    before = func(n // 2)
    result = []

    for i in before:
        result.append(' ' * (n // 2) + i + ' ' * (n // 2))

    for i in before:
        result.append(i + ' ' + i)

    return result

n = int(input()) # 3, 6, 12, 24
print(*func(n), sep = "\n")

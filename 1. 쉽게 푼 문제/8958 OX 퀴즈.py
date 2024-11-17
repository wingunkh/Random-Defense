n = int(input())

for _ in range(n):
    s = input()
    n = 0
    result = 0

    for i in s:
        if i == 'O':
            n += 1
            result += n
        else:
            n = 0

    print(result)

def calculate_sum(s):
    result = 0

    for i in s:
        if i.isdigit():
            result += int(i)

    return result

n = int(input())
a = [input() for _ in range(n)]

a.sort(key = lambda x: (len(x), calculate_sum(x), x))

print(*a, sep = "\n")

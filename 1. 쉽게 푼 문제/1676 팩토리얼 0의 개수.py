def factorial(n):
    result = 1

    for i in range(1, n+1):
        result *= i

    return result

n = int(input())
s = str(factorial(n))
s = s[::-1]
result = 0

for i in s:
    if i != '0':
        break

    result += 1

print(result)

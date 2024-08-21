s = input()
a = "1"
result = 0

for i in range(len(s) - 1):
    a += '0'

for i in range(1, len(s)):
    result += (i * 9 * 10 ** (i - 1))

result += len(s) * (int(s) - int(a) + 1)

print(result)

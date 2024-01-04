n = int(input())
s = input()
result = 0

for i in range(n):
    result += (ord(s[i]) - 96) * 31 ** i

print(result % 1234567891)

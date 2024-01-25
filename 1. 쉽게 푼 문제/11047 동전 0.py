import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.reverse()
result = 0

for i in a:
    if m >= i:
        result += m // i
        m %= i

print(result)

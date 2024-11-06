import sys
input = sys.stdin.readline

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

n = int(input())
tree = [int(input()) for _ in range(n)]
gap = [tree[i + 1] - tree[i] for i in range(n - 1)]
gcd = gap[0]
result = 0

for i in range(1, len(gap)):
    gcd = GCD(gcd, gap[i])

for i in gap:
    result += i // gcd - 1

print(result)

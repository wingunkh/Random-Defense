import sys
input = sys.stdin.readline

n = int(input())
a = sorted([int(input()) for _ in range(n)])

print(*a, sep = "\n")

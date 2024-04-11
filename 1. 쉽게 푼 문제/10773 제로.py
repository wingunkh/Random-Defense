import sys
input = sys.stdin.readline

k = int(input())
stack = []

for _ in range(k):
    n = int(input())

    if n:
        stack.append(n)
    else:
        stack.pop()

print(sum(stack))

from collections import deque

n = int(input())
q = deque([i for i in range(1, n + 1)])
result = []

while len(q) > 1:
    result.append(q.popleft())
    q.append(q.popleft())

result.append(q.popleft())

print(*result, sep = ' ')

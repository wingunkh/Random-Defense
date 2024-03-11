from collections import deque

n, k = map(int, input().split())
a = [i for i in range(1, n + 1)]
q = deque(a)
result = []

while q:
    for _ in range(k - 1):
        q.append(q.popleft())

    result.append(q.popleft())

print("<" + ', '.join(map(str, result)) + ">")

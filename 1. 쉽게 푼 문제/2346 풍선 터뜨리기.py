from collections import deque

n = int(input())
a = list(map(int, input().split()))
q = deque()

for i in range(1, n + 1):
    q.append((i, a[i - 1]))

while q:
    index, paper = q.popleft()
    print(index, end = ' ')

    if paper > 0:
        for _ in range(paper - 1):
            if q:
                q.append(q.popleft())
    else:
        for _ in range(-paper):
            if q:
                q.appendleft(q.pop())

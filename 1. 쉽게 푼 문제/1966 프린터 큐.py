from collections import deque

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    q = deque(map(int, input().split()))
    result = 1

    while True:
        if q[0] == max(q):
            if k == 0:
                print(result)
                break
            q.popleft()
            result += 1
        else:
            q.append(q.popleft())

        k = (k - 1) if k > 0 else (len(q) - 1)

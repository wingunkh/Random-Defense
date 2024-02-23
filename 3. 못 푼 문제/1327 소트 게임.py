from collections import deque

def bfs():
    q = deque()
    q.append((a, 0))
    visited.add(''.join(a))

    while q:
        now, depth = q.popleft()

        if now == target:
            return depth

        for i in range(n - m + 1):
            tmp = now[i:i + m]
            tmp = tmp[::-1]
            next = now[:i] + tmp + now[i + m:]
            next_str = ''.join(next)

            if next_str not in visited:
                q.append((next, depth + 1))
                visited.add(next_str)

    return -1

n, m = map(int, input().split())
a = list(input().split())
visited = set()
target = sorted(a)

print(bfs())

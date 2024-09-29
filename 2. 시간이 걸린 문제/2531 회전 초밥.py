from collections import deque

def extend_window(x):
    global sushi

    if count[x] == 0:
        sushi += 1

    count[x] += 1

def reduce_window(x):
    global sushi

    if count[x] == 1:
        sushi -= 1

    count[x] -= 1

n, d, k, c = map(int, input().split())
q = deque(list(int(input()) for _ in range(n)))
count = [0 for _ in range(d + 1)]
sushi = 0
result = 0

for i in range(k):
    target = q[i]
    extend_window(target)

for _ in range(n + 1):
    # 정답 갱신
    if count[c] == 0:
        result = max(result, sushi + 1)
    else:
        result = max(result, sushi)

    # 큐 확대
    if k >= len(q):
        break

    next = q[k]
    extend_window(next)

    # 큐 축소
    prev = q.popleft()
    reduce_window(prev)
    q.append(prev)

print(result)

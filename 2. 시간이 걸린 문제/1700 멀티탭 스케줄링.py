import sys

n, k = map(int, input().split())
a = list(map(int ,input().split()))
now = []
result = 0

for i in a:
    if len(now) == n:
        break

    if i not in now:
        now.append(i)

for i in range(n, k):
    if a[i] in now:
        continue

    when = [sys.maxsize for _ in range(n)]

    for j in range(i + 1, k):
        if a[j] in now:
            if when[now.index(a[j])] == sys.maxsize:
                when[now.index(a[j])] = j
                
    now[when.index(max(when))] = a[i]
    # 현재 멀티탭에 꽂혀 있는 전기용품 중 가장 나중에 사용할 전기용품을 제거

    result += 1

print(result)

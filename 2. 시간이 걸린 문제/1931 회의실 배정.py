import sys
input = sys.stdin.readline

n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
# 종료 시간 기준 오름차순 정렬
# 종료 시간이 같을 때 사작 시간 기준 오름차순 정렬
a.sort(key = lambda x: (x[1], x[0]))
end = 0
result = 0

for i in a:
    if i[0] >= end:
        result += 1
        end = i[1]

print(result)

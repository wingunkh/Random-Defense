import sys
input = sys.stdin.readline

def use(money):
    count = 0
    have = 0
    i = 0

    while i <= n - 1:
        if have >= a[i]: # 남은 돈으로 하루를 보낼 수 있을 경우
            have -= a[i] # 돈 사용
            i += 1 # 다음 날 
        else: # 남은 돈으로 하루를 보낼 수 없을 경우
            have = money # 남은 돈을 통장에 집어넣고 돈 인출
            count += 1 # 인출 횟수 증가

    return count

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
left, right = max(a), sum(a)
result = sys.maxsize

while left <= right:
    center = (left + right) // 2
    count = use(center)

    if count > m:
        left = center + 1
    else:
        result = min(result, center)
        right = center - 1

print(result)

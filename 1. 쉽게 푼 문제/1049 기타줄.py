import sys
input = sys.stdin.readline

n, m = map(int, input().split())
six = sys.maxsize
one = sys.maxsize
result = 0

for _ in range(m):
    x, y = map(int, input().split())
    six = min(six, x)
    one = min(one, y)

if n >= 6: # 6개 이상 남았을 경우
    if six / 6 <= one: # 패키지 구매가 이득일 경우
        result += six * (n // 6)
        n %= 6
    else: # 낱개 구매가 이득일 경우
        result += one * n
        n = 0
        
# 6개 미만 남았을 경우
if six <= one * n: # 하나의 패키지 구매가 이득일 경우
    result += six
    n -= 6
else: # 남은 수만큼 낱개 구매가 이득일 경우
    result += one * n
    n = 0

print(result)

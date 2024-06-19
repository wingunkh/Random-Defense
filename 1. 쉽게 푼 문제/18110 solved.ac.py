import sys
input = sys.stdin.readline

def round(n):
    if n - int(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)
# 파이썬의 round() 함수는 사사오입이 아닌 오사오입이기 때문에 round() 함수를 직접 구현해야 한다.
# 사사오입 : 4 이하의 숫자는 내림, 5 이상의 숫자는 올림
# 오사오입 : 5 미만의 숫자는 내림, 5 초과의 숫자는 올림
# ↳ 만약 반올림할 자릿수가 5일 경우 5의 앞자리가 홀수인 경우 올림, 짝수인 경우 내림

n = int(input())

if n == 0:
    print(0)
else:
    score = sorted([int(input()) for _ in range(n)])
    target = round(n * 0.15)

    if target > 0:
        score = score[target:-target]

    print(round(sum(score) / len(score)))

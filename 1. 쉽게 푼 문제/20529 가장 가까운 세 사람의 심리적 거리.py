import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(input().split())
    result = sys.maxsize

    if n > 32:
        print(0)
        continue
    # 비둘기집 원리
    # n개의 비둘기집에 n+1마리 이상의 비둘기를 넣으면,
    # 적어도 한 개의 비둘기집에는 2마리 이상의 비둘기가 존재
    # n > 16일 경우, 같은 MBTI 유형의 학생이 적어도 2명 존재
    # n > 32일 경우, 같은 MBTI 유형의 학생이 적어도 3명 존재 

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or i == k:
                    continue

                tmp = 0

                for l in range(4):
                    if a[i][l] != a[j][l]:
                        tmp += 1
                    if a[j][l] != a[k][l]:
                        tmp += 1
                    if a[i][l] != a[k][l]:
                        tmp += 1

                result = min(result, tmp)

    print(result)

n, m = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])
left, right = 1, a[-1] - a[0]
result = 0 # 최대 최소 간격

while left <= right:
    distance = (left + right) // 2 # 탐색 중인 최대 최소 간격
    count = 1
    # 첫 번째 집에는 무조건 공유기 설치, 따라서 count는 1로 시작
    now = 0
    # 현재 설치된 공유기의 위치를 표시하는 인덱스 (첫 번째 집에 설치)

    for i in range(1, n): # 두 번째 집부터 마지막 집까지 공유기 설치 시도
        if a[i] - a[now] >= distance: # 현재 집과 마지막으로 공유기 설치한 집 사이의 거리가 distance 이상일 경우
            count += 1  # 현재 집에 공유기 설치
            now = i

    if count >= m:  # 설치된 공유기 수가 목표치 m 이상일 경우
        result = distance # 최대 최소 간격 갱신
        left = distance + 1
    else:
        right = distance - 1

print(result)

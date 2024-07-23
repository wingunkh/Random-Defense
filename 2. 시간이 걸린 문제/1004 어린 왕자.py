t = int(input())

# 원의 방정식 : (x - a) ** 2 + (y - b) ** 2 = r ** 2
# (x - a) ** 2 + (y - b) ** 2 가 r ** 2 보다 작다면?
# 점 (x, y)는 중점이 (a, b)이고 반지름이 r인 원의 내부에 위치함을 의미
def func(x, y, a, b, r):
    return (x - a) ** 2 + (y - b) ** 2 < r ** 2
    

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    result = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())

        case1 = func(x1, y1, cx, cy, r)
        case2 = func(x2, y2, cx, cy, r)
        
        if case1 and not case2:
            result += 1
        elif case2 and not case1:
            result += 1
        # 출발점과 도착점 중 하나의 점만 원의 경계 내부에 위치해야 함
        
    print(result)

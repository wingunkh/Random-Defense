t = int(input())

for _ in range(t):
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    for i in b:
        if i in a: # set도 해시 테이블 기반으로 구현되므로, 검색 시간복잡도가 O(1)
            print(1)
        else:
            print(0)

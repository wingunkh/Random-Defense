import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = []

    for _ in range(n):
        a.append(input().rstrip())

    a.sort()
    # 문자열을 정렬 시 사전 순 정렬됨
    # ex) 123 444 1234 -> 123 1234 444
    # 즉, 접두어 관계에 있는 전화번호는 반드시 인접하게 됨

    for i in range(n - 1):
        if a[i] == a[i + 1][:len(a[i])]:
            print("NO")
            break
    else:
        print("YES")

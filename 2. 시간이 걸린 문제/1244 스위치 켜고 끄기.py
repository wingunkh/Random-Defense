import sys
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
m = int(input())
student = []

for _ in range(m):
    gender, target = map(int, input().split())
    student.append((gender, target))

for gender, target in student:
    if gender == 1:
        for i in range(1, n + 1):
            if i % target == 0:
                a[i] = 1 - a[i]
    else:
        a[target] = 1 - a[target]
        left, right = target - 1, target + 1

        while 1 <= left and right <= n and a[left] == a[right]:
            a[left] = 1 - a[left]
            a[right] = 1 - a[right]
            
            left -= 1
            right += 1

for i in range(1, n + 1):
    print(a[i], end = ' ')

    if i % 20 == 0: # 0 / n == 0, 0 % n == 0 임에 유의
        print()

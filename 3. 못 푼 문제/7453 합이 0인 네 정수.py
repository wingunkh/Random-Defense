import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ab, cd = [], []
result = 0

for i in range(n):
    for j in range(n):
        ab.append(a[i][0] + a[j][1])
        cd.append(a[i][2] + a[j][3])

ab.sort()
cd.sort()

left, right = 0, len(cd) - 1

while left <= len(ab) - 1 and right >= 0:
    sum = ab[left] + cd[right]

    if sum == 0:
        left += 1
        right -= 1
        count1, count2 = 1, 1

        while left <= len(ab) - 1 and ab[left] == ab[left - 1]:
            left += 1
            count1 += 1
        while right >= 0 and cd[right] == cd[right + 1]:
            right -= 1
            count2 += 1

        result += count1 * count2
    elif sum > 0:
        right -= 1
    else:
        left += 1

print(result)

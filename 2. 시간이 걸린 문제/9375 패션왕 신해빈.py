t = int(input())

for _ in range(t):
    n = int(input())
    dic = dict()
    result = 1

    for _ in range(n):
        _, kind = input().split()

        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1

    for i in dic:
        result *= dic[i]+1
        # (A 종류 수 + 1) * (B 종류 수 + 1) * (C 종류 수 + 1) ... - 1
        # 1을 더하는 이유 : 해당 종류의 의상을 착용하지 않는 경우를 고려
        

    print(result-1)
    # 1을 빼는 이유 : 모든 의상을 착용하지 않는 경우를 제외

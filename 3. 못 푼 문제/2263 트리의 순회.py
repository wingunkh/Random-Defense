import sys
sys.setrecursionlimit(10 ** 6)

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]
    left_count = a[root] - in_start
    right_count = in_end - a[root]

    print(root, end = ' ')
    
    preorder(in_start, in_start + left_count - 1,
             post_start, post_start + left_count - 1)
    # 왼쪽 서브 트리에 대해 전위 순회를 재귀적으로 호출
    # 중위 순회에서 왼쪽 서브 트리의 범위: 시작 인덱스 ~ (시작 인덱스 + 왼쪽 서브 트리의 노드 수 - 1)
    # 후위 순회에서 왼쪽 서브 트리의 범위: 시작 인덱스 ~ (시작 인덱스 + 왼쪽 서브 트리의 노드 수 - 1)
    preorder(in_end - right_count + 1, in_end,
             post_end - right_count, post_end - 1)
    # 오른쪽 서브 트리에 대해 전위 순회를 재귀적으로 호출
    # 중위 순회에서 오른쪽 서브 트리의 범위: (끝 인덱스 - 오른쪽 서브 트리의 수 + 1) ~ 끝 인덱스
    # 후위 순회에서 오른쪽 서브 트리의 범위: (끝 인덱스 - 오른쪽 서브 트리의 수) ~ (끝 인덱스 - 1)

n = int(input())
inorder = list(map(int, input().split()))
# 중위 순회
# 루트 노드 왼쪽 = 왼쪽 서브 트리
# 루트 노드 오른쪽 = 오른쪽 서브 트리
postorder = list(map(int, input().split()))
# 후위 순회
# 마지막 노드 = 루트 노드
a = [0 for _ in range(n + 1)]
# 중위 순회에서 각 노드가 위치한 인덱스를 저장하는 배열
# 후위 순회를 통해 루트 노드를 찾은 다음, 이 배열을 통해 왼쪽 서브 트리와 오른쪽 서브 트리를 분할

for i in range(n):
    a[inorder[i]] = i

preorder(0, n - 1, 0, n - 1)

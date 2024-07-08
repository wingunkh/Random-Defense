import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def init(start, end):
    if start >= end:
        return None

    root = a[start]
    left = start + 1
    right = end

    for i in range(left, end):
        if a[i] > root:
            right = i
            break

    tree[root] = {
        'left': init(left, right),
        'right': init(right, end)
    }

    return root

def postorder(node):
    if node is None:
        return
    
    postorder(tree[node]['left'])
    postorder(tree[node]['right'])
    
    print(node)

a = []
tree = {}

while True:
    try:
        x = int(input())
    except:
        break

    a.append(x)

init(0, len(a))
postorder(a[0])

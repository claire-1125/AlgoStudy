# 인접 리스트(딕셔너리 → 노드 이름이 알파벳)를 만들어야 한다.
tree = {}

for _ in range(int(input())):
    node, left, right = input().split()
    tree[node] = [left, right]

# 'tree'라서 겹치는 노드가 없으므로 사용할 필요가 없다.
# visited = [False] * n

# 전위 순회
def preOrder(node):
    if not node == '.':
        print(node,end="")
        preOrder(tree[node][0])  # left child
        preOrder(tree[node][1])  # right child

# 중위 순회
def inOrder(node):
    if not node == ".":
        inOrder(tree[node][0])  # left child
        print(node,end="")
        inOrder(tree[node][1])  # right child

# 후위 순회
def postOrder(node):
    if not node == ".":
        postOrder(tree[node][0])  # left child
        postOrder(tree[node][1])  # right child
        print(node,end="")


preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
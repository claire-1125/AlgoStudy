# 1번 시작, 갈 수 있는 노드 수? (cycle 제외)

n, m = map(int, input().split())  # node, edge
edges = [tuple(map(int, input().split())) for _ in range(m)]  # 연결된 노드들 리스트

# Write your code here!

# 인접 리스트
adjacent = [[] for _ in range(n+1)]  

for n1, n2 in edges:
    adjacent[n1].append(n2)
    adjacent[n2].append(n1)

# 방문 여부 체크
nodes = [0 for i in range(n+1)]
nodes[0] = -1

# (임시) 방문한 곳 출력
visited = []

def dfs(node):
    # 현재 노드 방문 처리
    nodes[node] = 1
    visited.append(node)
    

    # 인접한 노드에 대해 재귀
    for candi in adjacent[node]:
        if nodes[candi] == 0:
            dfs(candi)


dfs(1)

print(len(visited)-1)
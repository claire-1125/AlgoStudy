# # 입력 예
# 4 5 1  # node, edge, start
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# # 출력 예
# 1 2 4 3  # DFS
# 1 2 3 4  # BFS

from collections import deque

node, edge, start = map(int, input().split())

# edge 수 만큼 반복
# adjacent=[[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]
adjacent = [list(map(int, input().split())) for _ in range(edge)]

# 방문리스트
visited = [0]*(node+1)

dfs_result, bfs_result = [], []

# 매개변수: 인접리스트, 현재 노드, 방문리스트
def dfs(adj, now, visited):
    # 현재 노드 방문 처리
    visited[now] = 1
    dfs_result.append(str(now))

    # 현재 꺼낸 것에 대한 인접 노드 리스트 구하기
    now_adj = []

    for elem in adj:
        if now in elem:
            now_adj.extend(elem)

    now_adj = list(set(now_adj) - set([now]))

    # 인접 노드에 대해 재귀
    for candi in now_adj:
        if not visited[candi]:
            dfs(adj,candi,visited)



# 매개변수: 인접리스트, 시작노드, 방문리스트
def bfs(adj, start, visited):
    # 시작 노드 큐에 넣기 및 방문 처리
    queue = deque([start])
    visited[start] = 1
    bfs_result.append(str(start))

    # 큐가 빌 때까지
    while queue:
        # 하나 꺼내기
        now = queue.pop()

        # 현재 꺼낸 것에 대한 인접 노드 리스트 구하기
        now_adj = []

        for elem in adj:
            if now in elem:
                now_adj.extend(elem)

        now_adj = list(set(now_adj) - set([now]))


        # 인접한 것에 대해
        for candi in now_adj:
            if not visited[candi]:
                # 큐에 넣기
                queue.append(candi)
                # 방문 처리
                visited[candi] = 1
                bfs_result.append(str(candi))

    


dfs(adjacent,start,visited)
visited = [0]*(node+1)
bfs(adjacent,start,visited)

print(' '.join(dfs_result))
print(' '.join(bfs_result))
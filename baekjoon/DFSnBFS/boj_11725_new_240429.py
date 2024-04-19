# 트리의 부모?
# DFS 기준: 본인을 호출한 부모 노드
# BFS 기준: 인접 리스트?

# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7

# 4
# 6
# 1
# 3
# 1
# 4
from collections import deque


n = int(input())

adjacent = [list(map(int, input().split())) for _ in range(n-1)]

visited, result = [0]*(n+1), [0]*(n+1)

def bfs(adj, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        now = queue.pop()

        now_adj = []

        for elem in adj:
            if now in elem:
                now_adj.extend(elem)
        
        now_adj = list(set(now_adj) - set([now]))

        for candi in now_adj:
            if visited[candi]:
                result[now] = candi
            elif not visited[candi]:
                queue.append(candi)
                visited[candi]


bfs(adjacent, 1, visited)

print(result)
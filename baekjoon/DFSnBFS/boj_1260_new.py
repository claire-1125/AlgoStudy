from collections import deque

def dfs(visited,adjacent,now):
    visited[now] = 1
    print(now,end=" ")

    for elem in adjacent[now]:
        if not visited[elem]:
            dfs(visited,adjacent,elem)

def bfs(visited,adjacent,start):
    visited[start] = 1
    queue = deque([start])

    while queue:
        now = queue.popleft()
        print(now, end=" ")

        for elem in adjacent[now]:
            if not visited[elem]:
                queue.append(elem)
                visited[elem] = 1


node, edge, Start = map(int,input().split())
info = [[*map(int,input().split())] for _ in range(edge)]

# 방문여부
Visited = [0 for _ in range(node+1)]

# 인접 리스트
# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
Adjacent = [[] for i in range(node+1)]
for a,b in info:
    Adjacent[a].append(b)
    Adjacent[b].append(a)

# depth 동일하면 작은 수부터 방문
for i in range(1,node+1):
    Adjacent[i].sort()

dfs(Visited,Adjacent,Start)

# 방문여부 초기화 되어야 dfs 돌아간다...
Visited = [0 for _ in range(node+1)]
print()

bfs(Visited,Adjacent,Start)
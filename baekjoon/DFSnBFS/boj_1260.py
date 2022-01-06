"""
참고한 블로그 포스팅
https://goplanit.site/42.%20Algorithm(1260_py)/
"""

from collections import deque

# 순서대로 node 개수, edge 개수, 시작 node 번호
node,edge,start = map(int, input().split())

# 인접리스트 (1번부터 시작)
graph = [[] for _ in range(node+1)]

def dfs(v):
    visited[v] = True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    deq = deque([start])
    visited[start] = True

    while deq:
        here = deq.popleft()
        print(here, end=" ")
        for i in graph[here]:
            if not visited[i]:
                deq.append(i)
                visited[i] = True


# 인접리스트 생성
for _ in range(edge):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 인접 리스트의 각 원소를 정렬하기
for elem in range(1, node+1):
    graph[elem].sort()


visited = [False] * (node+1)
dfs(start)
print()
visited = [False] * (node+1)
bfs(start)
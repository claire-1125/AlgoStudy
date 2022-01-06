from collections import deque

def bfs(start):
    deq = deque([start])
    visited[start] = True

    while deq:
        here = deq.popleft()
        for i in graph[here]:
            if not visited[i]:
                deq.append(i)
                visited[i] = True


for _ in range(int(input())):
    # 순열의 길이 (node 개수)
    node = int(input())

    visited = [False] * (node + 1)

    # 인접 리스트
    graph = [[] for _ in range(node + 1)]

    # 인접리스트 생성
    for _ in range(node):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)


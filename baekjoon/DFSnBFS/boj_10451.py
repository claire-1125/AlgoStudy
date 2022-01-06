"""
- 방향 그래프임에 유의!
    - 인접 리스트를 만든 뒤 정렬만 하지 않는다면 방향은 표시되어 있는 꼴이다.
- 사이클 + DFS/BFS?
    - 지금 방문하려는 노드가 이미 방문한 경우(visited[v]==True) 이 때 count + 1
    - 즉, 함수 실행이 종료된 경우 count + 1
"""

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
    node = int(input())  # 순열의 길이 (node 개수)
    visited = [False] * (node + 1)
    graph = [[] for _ in range(node + 1)]  # 인접 리스트

    # 입력으로 주어지는 순열
    permut = list(map(int,input().split()))

    # 인접리스트 생성
    for idx,elem in zip(range(1,node+1),permut):
        graph[idx].append(elem)

    # 실제 문제를 위한 구현
    cnt = 0
    for elem in range(1, node + 1):
        if not visited[elem]:
            bfs(elem)
            cnt += 1
        else:
            continue

    print(cnt)
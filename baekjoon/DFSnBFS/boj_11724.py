"""
<내가 생각한 알고리즘>
결국 각 연결요소에 대해 DFS를 크게 한 번(재귀적으로 부르는 것은 생각하지 않았을 때) 호출하는 것이므로
DFS 함수 실행이 끝날 때마다 count를 1씩 증가시키면 연결요소의 개수를 구할 수 있을 것이다.

Q. 연결되지 않는 요소에도 접근하기 위해서는 어떻게 해야할까?
A. visited 배열을 이용해보자..!
"""
from collections import deque
import sys

# 순서대로 node 개수, edge 개수
node,edge = map(int, sys.stdin.readline().split())

visited = [False] * (node+1)

# 인접 리스트
graph = [[] for _ in range(node+1)]

def bfs(start):
    deq = deque([start])
    visited[start] = True

    while deq:
        here = deq.popleft()
        for i in graph[here]:
            if not visited[i]:
                deq.append(i)
                visited[i] = True

# 인접리스트 생성
for _ in range(edge):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 인접 리스트의 각 원소를 정렬하기
for elem in range(1, node+1):
    graph[elem].sort()

# 실제 문제를 위한 구현
cnt = 0
for elem in range(1,node+1):
    if not visited[elem]:
        bfs(elem)
        cnt += 1
    else:
        continue

print(cnt)
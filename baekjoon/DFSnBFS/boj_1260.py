from collections import deque

# 순서대로 node 개수, edge 개수, 시작 node 번호
node,edge,start = map(int, input().split())

"""
< 각 edge에 연결된 노드 정보 → 인접 리스트 >
1. 각 edge에 연결된 노드 정보(temp_graph) 뿐만 아니라 set 타입에 node 종류도 저장(nodes)하기
2. temp_graph에서 nodes의 각 elem이 있는 원소에 대해 그의 다른 node를 graph에 추가한다.
"""

temp_graph, nodes = list(), set()

for _ in range(edge):
    node1,node2 = map(int,input().split())
    temp_graph.append((node1,node2))
    nodes.add(node1)
    nodes.add(node2)

graph = [[]]

for num in nodes:
    temp_adjacent = []
    for elem in temp_graph:
        if num in elem:
            if elem[0] != num:
                temp_adjacent.append(elem[0])
            elif elem[1] != num:
                temp_adjacent.append(elem[1])
    graph.append(temp_adjacent)

"""
여기서부터 그래프 순회 시작!
"""
# visited = [False] * len(nodes)

def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    deq = deque([start])
    visited[start] = True

    while deq:
        here = deq.popleft()
        print(here, end=" ")
        for i in graph[here]:
            if not visited[i]:
                deq.append(i)
                visited[i] = True

visited = [False] * (len(nodes)+1)
dfs(graph,start,visited)
# print("\n")
visited = [False] * (len(nodes)+1)
bfs(graph,start,visited)
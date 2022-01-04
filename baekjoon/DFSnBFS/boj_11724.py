# 순서대로 node 개수, edge 개수
node,edge = map(int, input().split())

temp_graph = list()
for _ in range(edge):
    temp_graph.append(tuple(map(int,input().split())))

# 인접 리스트 생성
graph_adjacent = [[]]
for num in range(1,node+1):
    temp_adjacent = []
    for elem in temp_graph:
        if num in elem:
            if elem[0] != num:
                temp_adjacent.append(elem[0])
            elif elem[1] != num:
                temp_adjacent.append(elem[1])
    graph_adjacent.append(temp_adjacent)


def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

visited = [False] * (node+1)

cnt = 0
for elem in range(1,node+1):
    dfs(graph_adjacent,elem,visited)
    cnt += 1

print("\n",cnt)
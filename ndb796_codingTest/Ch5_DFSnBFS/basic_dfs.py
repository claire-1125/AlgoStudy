"""
stack으로 구현

<필요한 변수들>
- graph : 그래프의 인접 리스트
- v : 현재 node의 index
- visited : 방문한 node 리스트 (boolean list)

현재 node 방문 → 인접한 node를 재귀적으로 방문
"""


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v,end=" ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for elem in graph[v]:
        if not visited[elem]:
            dfs(graph, elem, visited)

# 인접 리스트 (이걸로 그래프 모양을 추정할 수 있다.)
# node 번호를 1번부터 시작하기 위해 첫번째 리스트 원소는 빈 리스트이다.
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
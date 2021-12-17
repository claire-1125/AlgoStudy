"""
queue로 구현한다.

<필요한 변수들>
- graph : 그래프의 인접 리스트
- start : 최초 시작 node의 index
- visited : 방문한 node 리스트

재귀 사용하지 않는다!
"""

"""
1.[초기세팅] start 들어간 deque 생성 & visited 방문 처리
2.deque가 빌 때까지
    현재 노드 pop(from front)
    꺼낸 얘의 인접한 노드들에 대해
        방문하지 않은 노드라면
            그 노드 append(from rear)
            visited 방문 처리
"""

from collections import deque

def bfs(graph,start,visited):
    deq = deque([start])
    visited[start] = True

    while deq:
        v = deq.popleft()
        print(v,end=" ")
        for elem in graph[v]:
            if not visited[elem]:
                deq.append(elem)
                visited[elem] = True


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

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
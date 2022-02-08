"""
DFS, BFS 문제이다.
받는 정보는 인접행렬
나는 그래프를 순회할 것이다.
"""

"""
본인 node 방문 → 인접한 node 중 방문하지 않았다면 재귀적으로 방문

여기서의 '인접'의 의미?

"""

"""
인접행렬 → 인접리스트 변환?
"""

# def dfs(r,c,computers):
#     computers[r][c] = 1
#
#     for
#

def solution(n, computers):
    cnt = 0
    graph = []
    graph_2 = []

    # 인접행렬 → 인접리스트 변환
    for i in range(n):
        for j in range(n):
            if i<j and computers[i][j] == 1:
                graph.append((i,j))

    # [(0, 1), (1, 2)]

    print(graph)

    return n - cnt

# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]


print(solution(n,computers))
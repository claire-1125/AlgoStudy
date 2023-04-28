"""
DFS 사용 → 재귀!
현재 노드 방문 → 인접한 얘들에 대해 재귀적으로 방문
범위 안의 위치인지도 확인해야 한다.
"""

def dfs(r, c):
    if not ((r in range(n)) and (c in range(m))):
        return False

    if graph[r][c] == 0:
        graph[r][c] = 1

        dfs(r - 1, c)  # 상
        dfs(r + 1, c)  # 하
        dfs(r, c - 1)  # 좌
        dfs(r, c + 1)  # 우

        return True
    else:  # 전에 방문했거나 혹은 벽인 경우
        return False


n, m = map(int, input().split())

# [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
graph = [list(map(int, input())) for _ in range(n)]

# 만들 수 있는 아이스크림 수
cnt = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1

print(cnt)
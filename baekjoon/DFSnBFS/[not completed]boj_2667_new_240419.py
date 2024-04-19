# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 3
# 7
# 8
# 9

n = int(input())

map_ = []

for _ in range(n):
    temp = []
    for pos in input():
        temp.append(int(pos))
    map_.append(temp)

# 단지 수: dfs/bfs를 호출한 횟수
# 각 단지 내 가구수: 한 번 순회할 때 방문한 노드 개수

visited = [[0] * n] * n


def dfs(cnt, now: tuple, visited):
    # 현재 노드 방문
    visited[now[0]][now[1]] = 0
    cnt += 1

    # 인접: 상하좌우
    dr, dc = [-1,+1,0,0], [0,0,-1,+1]

    for i in range(len(dr)):
        temp_r, temp_c = now[0] + dr[i], now[1] + dc[i]

        # 지도 범위 내 존재하는지 확인
        if not (-1 < temp_r < n and -1 < temp_c < n):
            continue

        # 순회 안 한 곳이라면
        if visited[temp_r][temp_c]:
            dfs(cnt, (temp_r, temp_c), visited)


cnt = 0
dfs(cnt, (0,0), visited)

print(cnt)


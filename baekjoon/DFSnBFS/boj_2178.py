from collections import deque

def bfs(r,c):
    # 상,하,좌,우
    adjacent_r = [-1,+1,0,0]
    adjacent_c = [0,0,-1,+1]

    # 초기 설정
    queue = deque([(r,c)])

    while queue:
        now = queue.popleft()

        for a in range(4):
            r,c = now[0]+adjacent_r[a], now[1]+adjacent_c[a]

            # 범위 내에 존재하는지 확인
            if not ((r in range(n)) and (c in range(m))):
                continue

            # 벽인 경우 무시
            if pos[r][c] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우
            if pos[r][c] == 1:
                pos[r][c] = pos[now[0]][now[1]] + 1
                queue.append((r,c))

    return pos[n-1][m-1]


n,m = map(int,input().split())

# 길의 정보 + 최소 누적 길이
pos = [[elem for elem in map(int,input())] for _ in range(n)]

print(bfs(0,0))
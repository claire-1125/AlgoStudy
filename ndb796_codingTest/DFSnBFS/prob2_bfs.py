from collections import deque

cnt = 0

def bfs(r,c):
    # 가는 칸마다 counting
    global cnt

    # 순서대로 상,하,좌,우
    adjacent_r = [-1,+1,0,0]
    adjacent_c = [0,0,-1,+1]

    # 시작 위치는 무조건 괴물이 없는 상황
    graph[r][c] = 0
    deq = deque([(r,c)])

    while deq:
        v = deq.popleft()
        cnt += 1
        for i in range(4):
            r,c = v[0] + adjacent_r[i], v[1] + adjacent_c[i]
            if not ((r in range(n)) and (c in range(m))):
                continue
            elif graph[r][c] == 1:
                deq.append((r,c))
                graph[r][c] = 0


# n * m 차원 받기
n,m = map(int,input().split())

# 미로 정보 입력 받기
graph = [list(map(int,input())) for _ in range(n)]

bfs(0,0)

print(cnt)
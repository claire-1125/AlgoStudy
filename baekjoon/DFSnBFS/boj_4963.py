import sys

sys.setrecursionlimit(99999)

def dfs(r,c):
    # 범위 안에 존재하는지 확인
    if not ((r in range(h)) and (c in range(w))):
        return False

    # 현재 노드 방문 처리
    if pos[r][c] == 1:
        pos[r][c] = 0

        # 근접한 노드 재귀 방문
        dfs(r-1, c)  # 상
        dfs(r+1, c)  # 하
        dfs(r, c-1)  # 좌
        dfs(r, c+1)  # 우
        dfs(r-1, c+1)  # 북동
        dfs(r-1, c-1)  # 북서
        dfs(r+1, c+1)  # 남동
        dfs(r+1, c-1)  # 남서

        return True
    else:
        return False


while True:
    w,h = map(int,input().split())
    if (w,h) == (0,0):
        break

    pos = [[elem for elem in map(int,input().split())] for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j):
                cnt += 1

    print(cnt)

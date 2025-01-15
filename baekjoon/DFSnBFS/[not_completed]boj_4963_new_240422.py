# 인접 리스트: 상하좌우 + 대각선           
def dfs(r, c):
    # 지도 내 존재하는지 확인하기 
    if not (0 <= r <= h and 0 <= c <= w):
        return False

    # 현재 노드 방문처리 (1: 땅, 0: 바다)
    if map_[r][c] == 1:
        map_[r][c] = 0

        # 인접 노드에 대해 재귀
        dfs(r-1,c)  # 상
        dfs(r+1,c) # 하
        dfs(r,c-1) # 좌
        dfs(r,c+1) # 우
        dfs(r-1,c-1) # 좌상
        dfs(r-1,c+1) # 우상
        dfs(r+1,c-1) # 좌하
        dfs(r+1,c-1) # 우하

        return True
    else:
        return False


while True:
    w,h = map(int, input().split())

    if w == 0 and h == 0:
        break
    else:
        map_ = [list(map(int, input().split())) for _ in range(h)]
        
        cnt = 0
        # 지도 내 섬 개수 카운팅
        for i in range(h):
            for j in range(w):
                if dfs(i,j):
                    cnt += 1

    print(cnt)





# (0,0) → (n-1,m-1) 이동하기
# 탈출 가능 여부(1/0) 출력

n, m = map(int, input().split())  # n*m map

# 뱀 있으면 0, 없으면 1
grid = [list(map(int, input().split())) for _ in range(n)]  # map

# 뱀 존재여부 표기가 햇갈려서 정반대로 변경 (1→0, 0→1)
# 뱀 없으면 0, 있으면 1
grid_ = [[1-pos for pos in row] for row in grid]

# Write your code here!
def dfs(r,c):
    # 현재 위치 방문
    grid_[r][c] = -1

    # 인접(아래, 오른쪽)에서 안 간 곳 방문
    dr, dc = [+1,0],[0,+1]  

    for i in range(2):
        r_ , c_ = r + dr[i], c + dc[i]

        # 지도 밖을 벗어나지 않으면 + 뱀이 없는 위치면 재귀
        condition = ((r_ in range(n)) and (c_ in range(m))) and (grid_[r_][c_] == 0)

        if condition:
            dfs(r_,c_)


dfs(0,0)

# 도착 위치 flag에 따른 결과 출력
if grid_[n-1][m-1] == -1:
    print(1)
else:
    print(0)



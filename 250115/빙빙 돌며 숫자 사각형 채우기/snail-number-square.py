n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]  # map의 초기 상태

# Write your code here!
r,c = 0,0  # 초기 위치
dr, dc = [0,+1,0,-1],[+1,0,-1,0]  # R, D, L, U
dir_ = 0  # 초기 방향

# R, D, L, U 반복 (0,1,2,3)
# 이미 지나간 곳은 가면 안 된다!: 지나간 곳 tracing 필요
# 지나간 곳 tracing: 1부터 increment 진행

cnt = 1  # map내 지나간 곳 숫자 (동시에 이동한 횟수)
arr[r][c] = cnt  # 시작 위치는 바로 카운팅하기

while True:
    r_, c_ = r + dr[dir_], c + dc[dir_]

    # map 범위 안에 있고, 아직 안 지나간 곳이라면
    condition = ((r_ in range(n)) and (c_ in range(m))) and (arr[r_][c_] == 0)

    if condition:
        # 실제로 지나가기
        r, c = r_, c_
        cnt += 1
        arr[r][c] = cnt
        
    else:
        # map 밖이거나 이미 지나간 곳인 경우: 방향 변경
        dir_ = (dir_ + 1) % 4  # index를 순환 순회하기 위해서 % 연산 이용


    # 모두 방문했다면 탈출!
    if all(0 not in row_ for row_ in arr):
        break

# 결과 출력
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
    


    


N, T = map(int, input().split())  # n은 홀수
str = input()  # T개 만큼의 명령어 (path)
board = [list(map(int, input().split())) for _ in range(N)]  # n*n의 map

# Write your code here!

r,c = N//2, N//2  # 시작위치

dr, dc = [-1,0,+1,0],[0,+1,0,-1]  # 이동 방향 정의 (북,동,남,서; 시계방향)
dir_num = 0  # 시작방향

tot_sum = board[r][c] # 지나간 경로의 숫자 더하기: 시작위치 포함

for i in range(T):
    if str[i] == 'R':
        # 우회전: 0->1, 1->2, 2->3, 3->0
        dir_num = (dir_num + 1) % 4
    elif str[i] == 'L':
        # 좌회전: 0->3, 3->2, 2->1, 1->0
        dir_num = (dir_num - 1) % 4
    else:
        r_,c_ = r+dr[dir_num], c+dc[dir_num]

        # map 내에 있는지 확인
        if ((r_ in range(N)) and (c_ in range(N))):
            r, c = r_, c_  # 해당 방향으로 이동
            tot_sum += board[r][c]  # 값 더하기

        

print(tot_sum)

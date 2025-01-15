# https://www.acmicpc.net/problem/2578
# 5*5 빙고판, 각 칸마다 1~25의 숫자 하나 적음
# 사회자가 부르는 수 하나씩 지우기
# 가로줄, 세로줄, 대각선 위 5개 지워지면 선을 긋는다.
# 그어진 선이 3개 이상인 경우 빙고
# 몇 번째 수를 부른 후 빙고를 외치게 되는지?

# 1~25의 수는 각 한번씩만 사용된다.


board = [list(map(int, input().split())) for _ in range(5)]
board_checked = [[0] * 5 for _ in range(5)]

called = [list(map(int, input().split())) for _ in range(5)]
called = [elem for row in called for elem in row] 

cnt = 0  # 부른 수 개수

called_idx = []



# 가로, 세로, 대각선 5개: 각 위치(index)를 알아야 함.
# 이미 체크한 것은 다시 체크해서는 안 됨

print(board)

for a in range(len(called)):
    # 부른 수 체크하기
    for i in range(len(board)):
        if called[a] in board[i]:
            j = board[i].index(called[a])
            board_checked[i][j] = 1
            called_idx.append((i,j))

    
    # 가로, 세로, 대각선 체크
    if (a+1) % 5 == 0:
        # 0,1,2,3,4,
        # 5,6,7,8,9,
        # 10,11,12,13

        # (a+1)//5 - 1

        # 이제까지의 인덱스 가져오기
        called_idx[:a]


        # 가로 체크
        for j in range(5):
            if board_checked[동일][j]:
                pass

        # 세로 체크
        for i in range(5):
            if board_checked[i][동일]:
                pass

        # 대각선 체크 (i,j 하나씩 증가)
        for i in range(5):
            for j in range(5):
                board_checked[i][j]

    # 부를 때마다 카운팅
    cnt += 1
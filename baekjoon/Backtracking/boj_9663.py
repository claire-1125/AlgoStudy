"""
<공부자료>
https://chanhuiseok.github.io/posts/baek-1/

<global을 쓰면 시간이 지체된다.>
https://8iggy.tistory.com/155

<테스트케이스>
n=4, 정답=2
n=8, 정답=92
"""

import sys
sys.setrecursionlimit(10000)

def promising(r, board):
    for j in range(r):
        # column이 동일 / row 단위의 차이와 column 단위의 차이가 동일
        if board[r] == board[j] or r - j == abs(board[r] - board[j]):
            return False
    return True

# 함수를 탈출하는 경우?
def nqueen(n, chessboard, row):
    print("row:",row)

    if row == n:  # 모든 queen을 배치한 경우
        print("here:",chessboard)
        print("=================")
        # count += 1
    else:
        for i in range(n):
            chessboard[row] = i  # 일단 queen을 놔본다.

            if promising(row, chessboard):  # 현재 위치가 놓으면 안 되는 자리인지 판단
                nqueen(n, chessboard, row + 1)  # 되는 자리이면 진행
            else:
                continue

n = int(input())
chessboard = [0] * n
result = 0
if nqueen(n, chessboard, 0):
    result += 1
# result += nqueen(n, chessboard, 0)
print("탈출!")
print(result)
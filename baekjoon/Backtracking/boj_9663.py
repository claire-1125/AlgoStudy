# https://chanhuiseok.github.io/posts/baek-1/
# 시간 덜 걸리는 방법?


chessboard = [0] * 15
count = 0

def promising(row):
    global chessboard

    for j in range(row):
        # column이 동일 / row 단위의 차이와 column 단위의 차이가 동일
        if chessboard[row] == chessboard[j] or row - j == abs(chessboard[row] - chessboard[j]):
            return False
    return True


def nqueen(n, row):
    global chessboard
    global count

    if row == n:  # 마지막 row인 경우
        count += 1

    else:
        for i in range(n):
            chessboard[row] = i  # 일단 queen을 놔본다.

            if promising(row):  # 현재 위치가 놓으면 안 되는 자리인지 판단
                nqueen(n, row + 1)  # 되는 자리이면 진행
            else:
                continue



nqueen(int(input()), 0)
print(count)
# https://mjmjmj98.tistory.com/150
# https://velog.io/@tjdud0123/%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80-%EC%97%B4%EC%87%A0-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python

# key의 rotation
# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
def rotateClockwise90(matrix):
    return zip(*matrix[::-1])  # 시계방향 90도

"""
반전    90도     180도   270도
1 1 1   1 0 1   0 0 1   1 1 0
0 1 1   0 1 1   1 1 0   1 1 0
1 0 0   0 1 1   1 1 1   1 0 1
"""

def solution(key, lock):
    answer = True

    k_len, l_len = len(key), len(lock)

    # key를 변환한 것
    key_ = key.copy()

    # key의 element-wise 반전 matrix
    # for row in range(len(key)):
    #     for col in range(len(key[0])):
    #         key_[row][col] = int(not key[row][col])

    # 자물쇠를 크게 만들기: 한 변 길이 2m + n - 2
    board = [[0] * (2*k_len+l_len-2) for _ in range(2*k_len+l_len-2)]
    for i in range(l_len):
        for j in range(l_len):
            board[i+(k_len-1)][j+(k_len-1)] = lock[i][j]


    # 시계방향으로 90도 회전할 때마다 이동하며 맞물리나 확인
    for _ in range(4):
        key_ = rotateClockwise90(key_)
        for a in range(k_len):
            for b in range(k_len):
                pass
                # if board[][] == key_[][]:
                #     continue
                # else:
                #     break

    return answer

Key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
Lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(Key, Lock))
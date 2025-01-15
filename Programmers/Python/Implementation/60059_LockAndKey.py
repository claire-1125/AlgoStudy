# https://mjmjmj98.tistory.com/150
# https://velog.io/@tjdud0123/%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80-%EC%97%B4%EC%87%A0-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python


# 회전 (rotation): clockwise 90도 회전
# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
def key_rotation(key):
    return list(zip(*key[::-1]))


# 실제 자물쇠 영역이 열쇠와 딱 맞물려서 열리는 상태인지 확인
def unlock_or_not(lock_, m, n):
    # padding을 씌운 자물쇠 내 실제 자물쇠 범위: [ 0+(m-1), {0+(m-1)}+n )
    for i in range(m-1,(m-1)+n):
        for j in range(m-1,(m-1)+n):
            if lock_[i-(m-1)][j-(m-1)] != 1:
                return False
            
    return True


def solution(key, lock):
    m, n = len(key), len(lock)

    # 자물쇠 주위로 열쇠 길이만큼 padding 놓기: 한 변당 2m+n-2
      # (2m+n-2)*(2m+n-2) 0 행렬 만든 뒤 가운데를 lock값으로 교체
      # lock이 들어갈 범위: [ 0+(m-1), {0+(m-1)}+n )
    lock_ = [[0]*(2*m+n-2) for _ in range(2*m+n-2)]

    for i in range(m-1,(m-1)+n):
        for j in range(m-1,(m-1)+n):
            lock_[i][j] = lock[i-(m-1)][j-(m-1)]


    # 각 위치마다 돌리고 확인
    for i in range(m-1,(m-1)+n):
        for j in range(m-1,(m-1)+n):
            # 회전: 90도, 180도, 270도, 360도 
            for _ in range(4):
                # 회전 (rotation): clockwise 90도 회전
                key_rotated = key_rotation(key)

                # 열쇠가 차지하는 영역에 대해 칸별로 값 더하기
                for a in range(m):
                    for b in range(m):
                        lock_[i+a][j+b] += key_rotated[a][b]

                # 실제 자물쇠 부분이 모두 1인지 확인
                if unlock_or_not(lock_, m, n):
                    return True

                # 다음 순회를 진행하기 위해 padding 넣은 자물쇠 원상복구
                for a in range(m):
                    for b in range(m):
                        lock_[i+a][j+b] -= key_rotated[a][b]

    return False

Key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
Lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(Key, Lock))
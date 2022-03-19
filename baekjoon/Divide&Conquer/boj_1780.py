N = int(input())

nums = [[elem for elem in map(int,input().split())] for _ in range(N)]

minus_ones, zeros, ones = 0,0,0

def dnc(r,c,n):
    """
    args
        - x, y : 각 구역의 좌측상단 좌표
        - n : 각 구역의 크기 (가로 길이)
    """

    global minus_ones, zeros, ones  # 재귀하므로 함수 내부에서 초기화 X

    standard = nums[r][c]  # 각 구역의 좌측상단 수 (기준 수)

    # 각 구역을 구성하는 숫자 체크 (linear search)
    for i in range(r,r+n):
        for j in range(c,c+n):
            if nums[i][j] != standard:  # 현재 구역이 두 가지 이상의 수로 구성된 경우
                new_n = n // 3  # 가로(세로)당 1/3배씩
                for a in range(3):
                    for b in range(3):
                        new_r, new_c = r + (new_n * a), c + (new_n * b)  # 분할될 각 구역의 좌측상단 좌표
                        dnc(new_r,new_c,new_n)  # 분할될 각 구역에 대해 재귀 (동일성 검사)
                return  # 재귀된 얘들이 돌아올 장소(?)

    # 해당 구역이 동일한 수로 구성된 경우 counting
    if standard == -1:
        minus_ones += 1
    elif standard == 0:
        zeros += 1
    else:
        ones += 1


dnc(0,0,N)
print(f'{minus_ones}\n{zeros}\n{ones}')

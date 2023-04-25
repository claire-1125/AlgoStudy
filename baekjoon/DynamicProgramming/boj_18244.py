import numpy as np

def solution(n):
    # dp table 생성 및 초기세팅
    # dp_table = [[0]*10 for _ in range(n+1)]

    # 'range'의 파라미터는 열(컬럼) → 행(로우) → 층(레벨)의 순서로 선언하면 되며,
    # 최초 초기화할 값(0, None...등)에 따라 선언이 완료된다.
    # dp_table = [[[0 for _ in range(10)] for _ in range(n+1)] for _ in range(5)]
    dp_table = np.zeros([5,(n+1),10])

    # 한자리수
    for j in range(10):
        dp_table[1][j][3] = 1

    # 두자리수 이상
    for i in range(1,n+1):
        for j in range(10):
            if j < 9:  # j==0도 가능
                # 1 감소
                # dp[i][j][2] = i-1 이고 j+1 이면서 d=3(증가X),d=4(1증가),d=5(2증가) 상태에서 올 수 있음.
                dp_table[i][j][2] += dp_table[i-1][j+1][3]
                dp_table[i][j][2] += dp_table[i-1][j+1][4]
                dp_table[i][j][2] += dp_table[i-1][j+1][5]

                # 2 감소
                # dp[i][j][1] = i-1 이고 j+1 이면서 d=2(1감소)상태에서만 올 수 있음.
                dp_table[i][j][1] += dp_table[i-1][j+1][2]
            if j > 0:  # j==9도 가능
                # 1 증가
                # dp[i][j][4] = i-1 이고 j-1 이면서 d=3(증가X),d=2(1감소),d=1(2감소) 상태에서 올 수 있음.
                dp_table[i][j][4] += dp_table[i-1][j-1][3]
                dp_table[i][j][4] += dp_table[i-1][j-1][2]
                dp_table[i][j][4] += dp_table[i-1][j-1][1]

                # 2 증가
                # dp[i][j][5] = i-1 이고 j-1 이면서 d=4(1증가)상태에서만 올 수 있음.
                dp_table[i][j][5] += dp_table[i-1][j-1][4]


            

    return sum(dp_table[n]) % 1000000007
    # return True

print(solution(int(input())))
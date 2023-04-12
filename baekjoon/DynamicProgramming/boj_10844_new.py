def solution(n):
    # dp table 생성 및 초기 세팅 (n=1인 경우는 hard-coding)
    # row: n자리 계단수, column: 각 n자리 계단수의 일의 자리 숫자
    dp_table = [[] for _ in range(n+1)]
    dp_table[1].extend([0,1,1,1,1,1,1,1,1,1])

    # n=1인 경우는 점화식 상으론 dp_table[0]에 접근해야 하는데 이건 불가능하므로
    if n > 1:
        for r in range(2,n+1):  # 역시나 2부터 iterate하는 이유는 위와 동일함.
            for c in range(10):  # 일의 자리 숫자 (0~9)
                if c == 0:  # 0으로 끝나는 계단수
                    dp_table[r].append(dp_table[r-1][c+1])
                elif c in range(1,9):
                    dp_table[r].append(dp_table[r-1][c-1] + dp_table[r-1][c+1])
                else:  # 9로 끝나는 계단수
                    dp_table[r].append(dp_table[r-1][c-1])


    return sum(dp_table[n]) % 1000000000

print(solution(int(input())))

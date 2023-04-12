"""
  0 1 2 3 4 5 6 7 8 9
1 1 1 1 1 1 1 1 1 1 1
2 1 2 2 2 2 2 2 2 2 1
3 2 3 4 4 4 4 4 4 3 2
4 2 5 6 6 6 6 6 6 5 2

1010  1210

8789  8989

0123x 2123
2323 4323
2343 4343
4543 6543x

2345x 4345
4545 6545
4565 6565
6765 8765x

3456x 5456
5656 7656
5676 7676
9876x 7876

2345x 4345
4545 6545
4565 6565
6765 8765x

4567x 6567
6767 8767
6787 8787
8987



0101 2101
2321 4321x
2121 0121

1012
1212 3212
5432x 3432
3232 1232



5678x 7678
9878 7878
9898 7898




기본 점화식은 동일
단지 거기서 조건을 추가해야 하는 듯.

"""


def solution(n):
    # dp table 생성 및 초기세팅
    dp_table = [[0]*10 for _ in range(n+1)]
    dp_table[1] = [1,1,1,1,1,1,1,1,1,1]  # 변형 계단수는 0으로 시작할 수 있다.


    """
      0 1 2 3 4 5 6 7 8 9
    1 1 1 1 1 1 1 1 1 1 1
    2 1 2 2 2 2 2 2 2 2 1
    3 2 3 4 4 4 4 4 4 3 2
    4 2 5 6 6 6 6 6 6 5 2
    """

    if n in (2,3):
        for r in range(2,n+1):
            for c in range(10):
                if c == 0:
                    dp_table[r][c] = dp_table[r-1][c+1]
                elif c in range(1,9):
                    dp_table[r][c] = dp_table[r-1][c-1] + dp_table[r-1][c+1]
                else:
                    dp_table[r][c] = dp_table[r-1][c-1]
    elif n > 3:
        for r in range(2,4):
            for c in range(10):
                if c == 0:
                    dp_table[r][c] = dp_table[r-1][c+1]
                elif c in range(1,9):
                    dp_table[r][c] = dp_table[r-1][c-1] + dp_table[r-1][c+1]
                else:
                    dp_table[r][c] = dp_table[r-1][c-1]
        for r in range(4,n+1):  # range()의 start값 문제...
            for c in range(10):
                if c in (0,9):
                    dp_table[r][c] = dp_table[r-1][c]
                else:  # c in range(1,9)
                    dp_table[r][c] = dp_table[r-1][c] + dp_table[r-2][c]
                # elif c == 1:
                #     dp_table[r][c] = dp_table[r-1][c] + dp_table[r-1][c-1]
                # elif c == 8:
                #     dp_table[r][c] = dp_table[r-1][c] + dp_table[r-1][c+1]
                # elif c in (2,3,4):
                #     dp_table[r][c] = dp_table[r-1][c] + dp_table[r-1][c-2]
                # elif c in (5,6,7):
                #     dp_table[r][c] = dp_table[r-1][c] + dp_table[r-1][c+2]


    print(dp_table)
    return sum(dp_table[n]) % 1000000007

print(solution(int(input())))
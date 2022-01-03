for _ in range(int(input())):  # 테스트 케이스 개수만큼 반복
    stickers = list()
    n = int(input())
    for _ in range(2):
        stickers.append(list(map(int, input().split())))

    """
    스티커의 점수를 넣는 배열을 동시에 DP table로 사용했다.
    """
    for c in range(1,n): # column에 대해서 돌림
        if c == 1:
            stickers[0][c] += stickers[1][c-1]  # 왼쪽 대각선 아래
            stickers[1][c] += stickers[0][c-1]  # 왼쪽 대각선 위 
        else:
            stickers[0][c] += max(stickers[1][c-1],stickers[1][c-2]) # 왼쪽 대각선 아래 혹은 그 왼쪽 것
            stickers[1][c] += max(stickers[0][c-1],stickers[0][c-2]) # 왼쪽 대각선 위 혹은 그 왼쪽 것

    print(max(stickers[0][n-1],stickers[1][n-1]))
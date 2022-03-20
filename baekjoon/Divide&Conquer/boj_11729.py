def hanoi(n, start, via, to):
    """
    args
        param n : 원판 개수
        param start : 원래 위치 (막대 번호)
        param via : start에서 to로 가기 위한 경유지 (막대 번호)
        param to : 옮겨갈 위치 (막대 번호)
    상황
        start에서 to로 via를 거쳐 총 n개의 원반을 운반
    """

    if n == 1:
        print(f'{start} {to}')
    else:
        hanoi(n-1, start, to, via)  # 나머지 원판들 묶음이 두 번째 막대로 옮겨진다.
        print(f'{start} {to}')  # 가장 큰 원판이 세 번째 막대로 옮겨진다.
        hanoi(n-1, via, start, to)  # 나머지 원판들 묶음이 세 번째 막대로 옮겨진다.


N = int(input())
print(2**N - 1)
hanoi(N,1,2,3)
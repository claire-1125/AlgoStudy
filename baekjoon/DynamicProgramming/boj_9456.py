for _ in range(int(input())):  # 테스트 케이스 개수만큼 반복
    stickers = list()
    n = int(input())
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    print(stickers)
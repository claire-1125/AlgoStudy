""""<논리흐름>
500원, 100원, 50원, 10원짜리 동전 무한 개
거스름돈 N원
거슬러줘야 할 최소한의 동전 개수?"""

"""1260
500 2...260
100 2...60
50 1...10
10 1...0"""

"""나눈 것의 몫만큼 count
나눈 것의 나머지로 다시 몫 구하기"""


# money = int(input())

def solution(money):
    cnt = 0
    for elem in [500, 100, 50, 10]:
        cnt += money // elem
        money %= elem
    return cnt

print(solution(int(input())))
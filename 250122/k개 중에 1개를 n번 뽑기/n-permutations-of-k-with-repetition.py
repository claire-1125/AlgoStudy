# 1~K에서 하나 추출 행위를 N번 반복
# 서로 다른 순서쌍의 개수
# from itertools import permutations, combinations

K, N = map(int, input().split())

# Write your code here!

# Dynamic Programming ~ Divide and Conquer
# 방법: 재귀, 순회

# 재귀: 종료 조건 + 재귀 호출
# 순열, 조합 만들 시 재귀함수 사용 가능


answer = []

def print_answer():
    for elem in answer:
        print(elem, end=' ')
    print()


def choose(curr_num):
    # 종료 조건
    if curr_num == N+1:
        print_answer()
        return

    # 재귀 호출
    for i in range(1,K+1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

choose(1)
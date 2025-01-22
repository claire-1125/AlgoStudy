K, N = map(int, input().split())

# Write your code here!

# 재귀: 종료 조건 + 재귀 호출
# 순열, 조합 만들 시 재귀함수 사용 가능

answer = []  # 결과를 담는 리스트

def print_answer():
    for elem in answer:
        print(elem, end=' ')
    print()


def choose(curr_num):
    # curr_num: 재귀 횟수 카운팅 (1부터 시작)
    # 'K진수 중 택1'을 N번 진행

    # 종료 조건
    if curr_num == N+1:  # curr_num은 1부터 시작, N번만큼 재귀할 때는 N+1이 됨.
        print_answer()  # 함수 호출 대신 밖에서 출력하려 하면 answer는 이미 비워져 있음.
        return

    # 재귀 호출
    for i in range(1,K+1):  # K진수에 대해서 택 1 진행  
        # 재귀를 계속 타다 맨 안 쪽에서 print_answer() 호출 뒤 맨 마지막 원소 삭제
        answer.append(i)
        choose(curr_num+1) 
        answer.pop()  # 맨 뒤에 있는 원소 빼내기만 함. (출력 X)

choose(1)
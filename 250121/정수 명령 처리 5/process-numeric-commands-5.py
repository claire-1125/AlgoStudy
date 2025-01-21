N = int(input())  # 명령 개수

command = []  # 명령어 리스트
num = [] # 인자 리스트

for _ in range(N):
    line = input().split()
    command.append(line[0])  # 명령어만 삽입
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))  # 인자만 삽입
    else:
        num.append(0)  # 인자로 들어올 수 있는 정수는 1부터

# Write your code here!
list_ = []

# 원소 삽입
def push_back(n):
    # n을 삽입한다.
    list_.append(n)
    return

# 맨 뒤 원소 삭제
def pop_back():
    list_.pop()
    return

# 현재 리스트 길이 출력
def size_():
    print(len(list_))
    return 

# k번째 숫자 출력
def get_(n):
    if not list_:
        print(0)
    else:
        print(list_[n-1])

    return 

# 명령어-함수 매핑
cmd_ftn_mapping = {
    'push_back': push_back,
    'pop_back': pop_back,
    'size': size_,
    'get': get_
}


# 순서대로 명령어 실행
for i in range(N):
    present_cmd = cmd_ftn_mapping[command[i]]
    
    # 함수 호출
    if present_cmd == push_back or present_cmd == get_:
        present_cmd(num[i])
    else:
        present_cmd()
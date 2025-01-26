n = int(input())

answer = []

def beautiful_num(candi, candi_length):
    # candi: 현재 만들고 있는 숫자부분 (e.g. 333을 만드는 과정 중에서의 33)
    # candi_length: 현재 만들고 있는 숫자부분의 길이

    # 탈출 조건
    if candi_length == n:  # 현재 만들고 있는 숫자가 n만큼이 되면
        answer.append(candi)  # 아름다운 수가 되었으므로 정답 리스트에 추가
        return  # 현재 경로로는 더 진행할 수 없으므로 back!

    # 재귀 호출
    for sub_num in range(1,5):  # 뒤에 붙이게 될 숫자 (1,22,333,4444)
        # 뒤에 숫자를 더 붙여도 길이가 n을 넘지 않는다면
        if candi_length + sub_num <= n:  # 1이면 1자리 증가, 22면 2자리 증가, ...
            beautiful_num(candi+(str(sub_num)*sub_num), candi_length+sub_num)


# 아무 숫자도 만들지 않았으므로 빈 문자열, 길이는 0
beautiful_num("", 0)


print(len(answer))


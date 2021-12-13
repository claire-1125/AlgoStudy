"""
무조건 왼쪽에서부터 연산을 적용한다!
최대한 큰 수를 만든다
"""

num_list = list(map(int,input()))
"""
02984라고 입력한 경우
num_list = [0,2,9,8,4]
"""

result = 0
for elem in num_list:
    # 이전의 연산 결과에서 더하는 게 더 큰지 곱하는게 더 큰지 결정해서 overwrite
    result = max(result+elem, result*elem)

print(result)

# # 입력 예
# K1KA5CB7
# # 출력 예
# ABCKK13

# # 입력 예
# AJKDLSI412K4JSJ9D
# # 출력 예
# ADDIJJJKKLSS20


# 한 문자씩 문자인지, 숫자인지 확인하기: isalpha, isdigit
input_str = [elem for elem in input()]
only_alpha, only_digit = [], []

# 알파벳, 숫자 따로 리스트에 저장
for elem in input_str:
    if elem.isalpha():
        only_alpha.append(elem)
    elif elem.isdigit():
        only_digit.append(int(elem))


print(''.join(sorted(only_alpha)) + str(sum(only_digit)))
def solution(s):
    answer = ''
    totSum = 0
    totStr = []

    for elem in s:
        if elem.isdigit():
            totSum += int(elem)

        if elem.isalpha():
            totStr.append(elem)

    answer += ''.join(sorted(totStr))
    answer += str(totSum)

    return answer

# 예상 출력: ABCKK13
# S = 'K1KA5CB7'

# 예상 출력: ADDIJJJKKLSS20
S = 'AJKDLSI412K4JSJ9D'

print(solution(S))
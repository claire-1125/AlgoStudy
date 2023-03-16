def solution(s):
    # parenthesis = [elem for elem in s]

    parenthesis = []
    for elem in s:
        if parenthesis:
            if elem == '(':
                parenthesis.append(elem)
            else:
                if parenthesis[-1] == '(':
                    parenthesis.pop()
                else:
                    parenthesis.append(elem)
        else:
            parenthesis.append(elem)

    # parenthesis = []
    # for elem in s:
    #     # empty list의 경우 indexing 불가, slicing 가능
    #     if elem == ')' and parenthesis[-1:] == '(':
    #         parenthesis.pop()
    #     else:
    #         parenthesis.append(elem)

    return not parenthesis

S = "()()"
# S = "(())()"
# S = ")()("
# S = "(()("

print(solution(S))

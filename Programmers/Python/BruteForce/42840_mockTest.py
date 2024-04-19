def solution(answers):
    # 각 수포자의 제출답안 리스트 생성
    dropOut1 = [1,2,3,4,5] * (10000//5)
    dropOut2 = [2,1,2,3,2,4,2,5] * (10000//8)
    dropOut3 = [3,3,1,1,2,2,4,4,5,5] * (10000//10)

    # 각 수포자의 맞은 개수 counting
    result = [0,0,0]

    for a,b,c,d in zip(answers,dropOut1,dropOut2,dropOut3):
        if b == a:
            result[0] += 1
        if c == a:
            result[1] += 1
        if d == a:
            result[2] += 1


    maxCorrect = max(result)
    return [i+1 for i in range(len(result)) if result[i] == maxCorrect]


Answers = [1,2,3,4,5]
# Answers = [1,3,2,4,2]

print(solution(Answers))


import math

def solution(progresses, speeds):
    minus_progresses = [100-elem for elem in progresses]
    days = [math.ceil(a/b) for a,b, in zip(minus_progresses,speeds)]

    answer = []
    temp_list = [100]
    cnt = 0

    for elem in days:
        if temp_list[-1:] < [elem]:
            while not temp_list:
                temp_list.pop()
                cnt += 1
            answer.append(cnt)
        temp_list.append(elem)

    return answer


Progresses = [93, 30, 55]
Speeds = [1, 30, 5]

# Progresses = [95, 90, 99, 99, 80, 99]
# Speeds = [1, 1, 1, 1, 1, 1]

print(solution(Progresses, Speeds))

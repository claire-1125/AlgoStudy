import itertools

def solution(numbers, target):
    answer = 0
    step = 1

    if len(numbers) % 2 == 0:
        if target % 2 == 0:
            step = len(numbers) - target - 1
            answer = itertools.combinations(range(1, len(numbers), step),r)
        else:
            answer = 0
    else:
        if target % 2 == 0:
            answer = 0
        else:
            answer = itertools.combinations(range(1, len(numbers), step),r)

    return answer

numbers = [1,1,1,1,1]
target = 3
solution(numbers,target)
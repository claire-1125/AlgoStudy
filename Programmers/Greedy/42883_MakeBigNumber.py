from itertools import combinations

def solution(number, k):
    answer = ''
    candidate = list(combinations(number,len(number)-k))
    temp = ''

    # 합쳐서 overwrite하고 싶다...
    for elem in candidate:
        print("before:",elem)
        for i in elem:
            temp += i
        elem = int(temp)
        temp = ''
        print("after:",elem)

    print(candidate)
    return answer

number = "1924"
k = 2
# number = "1231234"
# k = 3
# number = "4177252841"
# k = 4

solution(number, k)
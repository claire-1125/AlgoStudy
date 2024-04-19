from itertools import permutations
import math

def isPrimeNumber(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False

    return True

def solution(numbers):
    answer = []

    # 문자열 상태의 숫자 종이 조각
    numberCards = [*numbers]

    # 순열 결과를 담을 배열
    result = []

    # 각 숫자 조각에 대한 순열 (1장 ~ 모두 다)
    for i in range(1, len(numbers)+1):
        result.extend([*permutations(numberCards, i)])

    """
    numbers = "17"
    result = [('1',),('7',),('1','7'),('7','1')]
    """

    for elem in result:
        pass
        tempNum = int(''.join(elem))
        # 소수 판별
        if isPrimeNumber(tempNum):
            answer.append(tempNum)


    # 중복 없애기 위해 set으로 type casting
    return len(set(answer))


Numbers = "17"
# Numbers = "011"

print(solution(Numbers))
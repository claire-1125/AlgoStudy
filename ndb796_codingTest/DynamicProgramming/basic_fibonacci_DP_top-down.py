"""
- 피보나치 수열 : 앞의 두 항의 합으로 이루어진 수열
- 이를 구현하기 위해선... 각 항의 값을 배열에 저장
- 배열의 index는 각 항의 번호(subscript)를 의미함.
- top-down : 재귀!
"""

# 각 항의 값을 저장하기 위한 배열 (index 0은 사용하지 않는다!)
d = [0] * 101

# d[1], d[2]에는 1이 들어가지는 않으나 d[3]부터는 제대로된 값이 들어간다.
def fibo(num):
    if num == 1 or num == 2:
        return 1

    if d[num] != 0:
        return d[num]

    d[num] = fibo(num-1) + fibo(num-2)
    return d[num]

print(fibo(99))

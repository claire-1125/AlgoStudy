# https://eunhee-programming.tistory.com/135
# https://wooono.tistory.com/545

def solution(s):
    answer = 0
    # i개씩 묶어보자
    for i in range(1,len(s)+1):
        for n in range((len(s)//i)+1):
            print(s[n*i:(n+1)*i])
            # 본인 앞뒤로 반복되나 확인




    return answer

"""
s[:i],s[i:2*i],s[2*i:3*i]
        s[:2],s[2:4],s[4:6]
"""

S = "aabbaccc"
# S = "ababcdcdababcdcd"
# S = "abcabcdede"
# S = "ab ca bc ab ca bc de de de de de de"
# S = "xababcdcdababcdcd"

print(solution(S))
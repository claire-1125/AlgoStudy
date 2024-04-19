# "aabbaccc" : 7
# "ababcdcdababcdcd": 9
# "abcabcdede": 8
# "abcabcabcabcdededededede": 14
# "xababcdcdababcdcd": 17

import math

s = input()

# n개 단위로 문자를 보자. (n은 내부적으로 increment해야하는 것)
# n의 범위: 1부터 문자열 길이 절반(버림)까지
# aabbaccc
# 2개 단위: aa: s[0:2], bb: s[2:4], ac: s[4:6],  cc: s[6:8]
# 다음 단위가 지금 단위랑 동일한가? zip() 함수 이용
# for a, b in zip([aa,bb,ac,cc], [bb,ac,cc]):
# 동일할 경우 cnt += 1, 다르면 cnt = 1 (기본 1번씩은 존재하므로)
# 결과문자열은 따로 저장 → 순회 돌면서 숫자+단위문자 결과 붙이기


temp_list = []  # 문자열 s를 단위길이로 자른 것
compression_length = []  # 각 단위길이로 압축했을 때의 길이 저장하는 리스트
cnt = 1  # 각 단위길이 반복횟수 카운팅
compressed_str = ''  # 각 단위길이로 압축할 때의 결과 문자열

for n in range(1,math.floor(len(s)/2)+1):
    for i in range(0,len(s),n):
        temp_list.append(s[i:i+n])


    for a,b in zip(temp_list[:], temp_list[1:]):
        if a == b:
            cnt += 1
        else:
            if cnt == 1:  # 한 번만 나오고 바로 다른 문자단위인 경우
                compressed_str += a
                cnt = 1
            else:  # 여러 번 반복된 단위가 종료된 경우
                compressed_str += str(cnt) + a
                cnt = 1

    
    

    # # 나머지 존재하는 경우 처리하기
    
    # if cnt == 1:  # 한 번만 나오고 바로 다른 문자단위인 경우
    #     compressed_str += a
    # else:  # 여러 번 반복된 단위가 종료된 경우
    #     compressed_str += str(cnt) + a

    # 초기화
    temp_list.clear()
    # cnt = 1
    
    print(compressed_str)
    
    
    print("=====================")






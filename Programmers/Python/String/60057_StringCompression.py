def solution(s):
    answer = []  # 각 문자 단위로 쪼갤 때의 길이값을 저장하는 배열

    # 애초에 문자열 길이가 1이면 1로 return
    if len(s) == 1: return 1

    # 문자열을 특정 문자 단위로 잘라주기
    for n in range(1,(len(s)//2)+1):  # 문자 단위 n
        tot_str = ''  # 현재 결과 문자열을 담는 변수
        cnt = 1  # 대상이 되는 단위 문자열이 몇 번 나오는가 counting
        temp_unit = s[:n]  # 대상이 되는 단위 문자열 (초기값은 맨 앞에 n자리)

        for i in range(n,len(s),n):  # 현재 단위 문자열을 위한 iterator/중요한 것은 temp_unit의 초기값이 맨 앞 n자리 이므로, 여기서는 그 다음 n자리부터 봐야 한다.
            if temp_unit == s[i:i+n]:  # 현재 단위 문자열과 대상 문자열이 일치하다면
                cnt += 1
            else:
                # cnt가 1인 경우는 표시하지 않으므로 따로 처리해야 한다.
                if cnt == 1:
                    tot_str += temp_unit
                else:
                    tot_str += str(cnt)+temp_unit

                temp_unit = s[i:i+n]  # 현재 단위 문자열이 새로운 대상 단위 문자열
                cnt = 1  # 새로운 대상 단위 문자열로 counting을 다시 시작해야 하므로 초기화


        # 남아있는 문자열에 대해서 처리
        if cnt == 1:
            tot_str += temp_unit
        else:
            tot_str += str(cnt) + temp_unit

        # 현재 압축시킨 최종 문자열의 길이를 저장
        answer.append(len(tot_str))

    return min(answer)


S = "aabbaccc"  # 7
# S = "ababcdcdababcdcd"  # 9
# S = "abcabcdede"  # 8
# S = "ab ca bc ab ca bc de de de de de de"  # 14
# S = "xababcdcdababcdcd"  # 17

print(solution(S))
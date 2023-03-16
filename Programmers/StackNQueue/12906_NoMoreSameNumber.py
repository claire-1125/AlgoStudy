def solution(arr):
    # 최종 출력할 원소를 담는 리스트
    answer = []

    for elem in arr:
        # answer 비어있나 확인
        if answer:
            # answer의 top이 elem과 동일한지 확인
            if answer[-1] != elem:
                answer.append(elem)
            else:
                continue
        else:
            answer.append(elem)

    return answer

# Arr = [1,1,3,3,0,1,1]
Arr = [4,4,4,3,3]
print(solution(Arr))
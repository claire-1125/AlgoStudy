# 컨테이너란?
#   다른 두 개의 단어로 구성 (바깥단어 + 안단어)
#   바깥단어를 두 개로 쪼갤 때, 각 길이는 상관없음.
#   단지 쪼갠 두 단어가 공백이지만 않으면 된다.
# 각 단어의 컨테이너 여부 출력?


# 실제로 사용할 때는 주로 리스트화 하여 사용한다.
from itertools import permutations  # 순열 (순서 고려)
# from itertools import combinations  # 조합 (순서 고려 X)
# from itertools import product  # 카테시안 곱 (여러 리스트 간 조합 경우의 수)

num_of_dict = int(input())
wordDict = [input() for _ in range(num_of_dict)]

container_list = []

# 아래 리스트에 바깥단어, 안단어 동일한 케이스 추가하기
permu_list = list(permutations(wordDict, 3))
permu_list_ = permu_list.copy()  # shallow copy? deep copy? 내가 원하는 것은 deep copy!

for elem in permu_list:
    permu_list_.append((elem[0], elem[0], elem[2]))

# [바깥단어, 안단어, 컨테이너(후보)]
for elem in permu_list_:
    # 바깥단어: elem[0], 안단어: elem[1], 컨테이너: elem[2]

    for i in range(len(elem[0])):
        sub1, sub2 = elem[0][:i+1], elem[0][i+1:]  # 바깥단어 분리
        if len(sub1) > 0 and len(sub2) > 0:
            if sub1 + elem[1] + sub2 == elem[2]:  # 바깥단어 + 안단어 = 컨테이너 인 경우
                container_list.append(elem[2])
        
container_list = set(container_list)

# 결과 출력
for word in wordDict:
    if word in container_list:
        print("Yes")
    else:
        print("No")
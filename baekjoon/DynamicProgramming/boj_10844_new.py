n = int(input())

# 길이가 1~ n-1인 계단수를 저장하기 위해 2차원 배열
# row의 index 자체가 특정 길이를 나타냈으면 좋겠다.
stairNum = [[] for _ in range(n+1)]

# 한 자리수인 계단수는 그냥 따로 구해야 한다.
stairNum[1] = [elem for elem in range(1, 10)]

# 길이가 1인 것부터 n인 것인 순서로 구해야 하므로 for문 이용: 상향식
for i in range(2,n+1):
    for elem in stairNum[i-1]:
        # 맨 뒤의 값만 가져오기
        lastNum = int(str(elem)[-1])
        for j in range(10):
            if abs(lastNum-j) == 1:
                stairNum[i].append(int(f'{elem}{j}'))

print(len(stairNum[n])%1000000000)
tot_cnt = 0

def dfs(nums,target,idx,cumSum):
    if idx == len(nums):  # traversal이 끝난 경우
        if cumSum == target:  # 타겟 넘버를 맞춘 경우
            global tot_cnt
            tot_cnt += 1  # 경우의 수 counting
        return
    else:  # traversal 진행 중
        dfs(nums,target,idx+1,cumSum+nums[idx])  # 다음 원소, 누적값±(현재의 값)로 재귀
        dfs(nums,target,idx+1,cumSum-nums[idx])

def solution(numbers, target):
    dfs(numbers,target,0,0)
    return tot_cnt

# 예상 출력: 5
# Numbers = [1, 1, 1, 1, 1]
# Target = 3

# 예상 출력: 2
Numbers = [4, 1, 2, 1]
Target = 4

print(solution(Numbers, Target))
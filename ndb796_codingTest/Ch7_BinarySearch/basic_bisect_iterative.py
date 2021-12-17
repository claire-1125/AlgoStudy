nums = sorted(list(map(int, input().split())))
searchNum = int(input())
left, right = 0, len(nums) - 1

while left <= right:
    middle = (left + right) // 2

    if searchNum < nums[middle]:
        right = middle - 1
    elif searchNum == nums[middle]:
        print("I found it!")
        print("index:",middle)
        break
    else:
        left = middle + 1


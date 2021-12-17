def binary_search_recursive(nums, searchNum, left, right):
    if left > right:
        return False

    middle = (left + right) // 2

    if searchNum < nums[middle]:
        return binary_search_recursive(nums,searchNum,left,middle-1)
    elif searchNum == nums[middle]:
        return middle
    else:
        return binary_search_recursive(nums,searchNum,middle+1,right)

nums = sorted(list(map(int, input().split())))
searchNum = int(input())
left, right = 0, len(nums) - 1
result = binary_search_recursive(nums,searchNum,left,right)
if not result:
    print("not in here")
else:
    print("index:",result)




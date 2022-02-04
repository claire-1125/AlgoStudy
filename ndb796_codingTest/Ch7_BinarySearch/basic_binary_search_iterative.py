def BinarySearchIterative(array, searchNum, left, right):

    while left <= right:
        middle = (left + right) // 2

        if array[middle] > searchNum:
            right = middle -1
            continue
        elif array[middle] < searchNum:
            left = middle + 1
            continue
        else:
            return middle
    return False


# 원소의 개수, 원하는 수
n, searchNum = map(int,input().split())

nums = [elem for elem in map(int,input().split())]

# 초기 설정
left, right = 0, n-1

result = BinarySearchIterative(nums,searchNum,left,right)

if not result:
    print("원소가 존재하지 않습니다.")
else:
    print(result)
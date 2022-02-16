def solution(n, times):
    left, right = 1, n*max(times)

    while left <= right:
        middle = (left + right) // 2

        cnt = 0
        for elem in times:
            cnt += middle // elem

        if n <= cnt:
            right = middle - 1
        else:
            left = middle + 1

    return left


print(solution(6,[7,10]))
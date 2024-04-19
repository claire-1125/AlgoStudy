def solution(my_string, n):
    answer = []
    for elem in my_string:
        for _ in range(n):
            answer.append(elem)

    return "".join(answer)

my_string = "hello"
n = 3

print(solution(my_string, n))

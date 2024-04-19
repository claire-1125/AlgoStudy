def solution(my_string):
    answer = [my_string[i] for i in range(len(my_string)-1,-1,-1)]
    return "".join(answer)


# my_string = "jaron"
my_string = "bread"

print(solution(my_string))
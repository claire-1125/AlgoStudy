def solution(s):
    return (len(s) in (4,6)) and s.isdigit()

# S = "a234"
# S = "1234"
# S = "123456"
S = "1269a"

print(solution(S))
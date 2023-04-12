import re

def solution(logs):
    answer = 0  # 수집하는 로그 counting

    # 안 되는 것: 숫자, 공백문자, 특수기호 / 되는 것: 알파벳
    placeholder = re.compile(r"team_name : ^[a-zA-Z]*$ application_name : ^[a-zA-Z]*$ error_level : ^[a-zA-Z]*$ message : ^[a-zA-Z]*$")


    for log in logs:
        result = placeholder.match(log)
        if result and (1 <= len(log) <= 200):  # 규칙에 맞는 경우 + 각 로그 길이가 200 이하
            answer += 1
        # else:  # 규칙 안 맞는 경우
        #     answer += 1

    return len(logs) - answer

# 예상 출력: 3
Logs = ["team_name : db application_name : dbtest error_level : info message : test",
        "team_name : test application_name : I DONT CARE error_level : error message : x",
        "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndWillTestForever",
        "team_name : oberevability application_name : LogViewer error_level : error"]

# 예상 출력: 6
# Logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange",
#         "no such file or directory",
#         "team_name : recommend application_name : recommend error_level : info message : RecommendSuccess11",
#         "team_name : recommend application_name : recomment error_level : info message : Success!",
#         "  team_name : db application_name : dbtest error_level : info message : test",
#         "team_name  : db application_name : dbtest error_level : info message : test",
#         "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]



print(solution(Logs))

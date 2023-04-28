def solution(msg):
    idxList = []

    # 단어 사전 기본 세팅
    wordDict = {}

    key = range(ord("A"), ord("Z")+1)
    value = range(1, 27)

    for k,v in zip(key, value):
        wordDict[chr(k)] = v


    # 혹시해서 모두 대문자로 변경
    msg_ = msg.upper()


    # 현재 대상 문자에 한 글자를 더 붙이는 것까지 조회를 해야 한다...
    for i in range(len(msg)):
        if msg[i] in wordDict:
            idxList.append(wordDict[msg[i]])
        else:
            pass

        if msg[i:i+2] in wordDict:
            continue
        else:
            idxList.append(wordDict[msg[i:i+2]])


    return idxList




Msg = "KAKAO"  #[11, 1, 27, 15]
# Msg = "TOBEORNOTTOBEORTOBEORNOT" # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# Msg = "ABABABABABABABAB" # [1, 2, 27, 29, 28, 31, 30]



print(solution(Msg))
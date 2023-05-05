def solution(msg):
    idxList = []

    # 단어 사전 기본 세팅
    wordDict = {}

    key = range(ord("A"), ord("Z")+1)
    value = range(1, 27)

    for k,v in zip(key, value):
        wordDict[chr(k)] = v

    # 단어 index 값 자동으로 increment하기 위한 용도
    # wordList = [(1, 'A'), (2, 'B'), (3, 'C'), ...]
    wordList = []
    for v, k in zip(list(wordDict.values()), list(wordDict.keys())):
        wordList.append((v,k))


    # 혹시해서 모두 대문자로 변경
    msg_ = msg.upper()

    # 현재 입력(w)의 길이가 가변적...
    for i in range(len(msg_)):
        # 현재 입력(w)이 어디까지인지를 알아야 하므로 시작점부터 한 글자씩 늘린다.
        # 사전에 있는 범위 내 가장 큰 단위글자만 찾아야 한다. e.g.) KA'KA'O (O) / KA'K'AO (X)
        for a in range(1,len(msg_)):
            here = msg_[i:i+a]  ### KAO까지 잘 가고 그 다음에 O가 아닌 A로 간다....
            if msg_[i:i+a] in wordDict:
                continue
            else:
                break  # w+c가 사전에 없는 순간 탈출

        # 탈출 직전까지가 현재 입력(w)
        idxList.append(wordDict[msg_[i:i+(a-1)]])  # 현재 글자의 색인 번호


        if msg_[i:i+a] in wordDict:  # 현재 입력 + 다음 글자 (w+c)가 있는가?
            continue
        else:
            # w+c가 없으면 사전 추가
            newIncre = wordList[-1][0]+1
            wordDict[msg_[i:i+a]] = newIncre
            wordList.append((newIncre, msg_[i:i+a]))


    return idxList




Msg = "KAKAO"  #[11, 1, 27, 15]
# Msg = "TOBEORNOTTOBEORTOBEORNOT" # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# Msg = "ABABABABABABABAB" # [1, 2, 27, 29, 28, 31, 30]



print(solution(Msg))
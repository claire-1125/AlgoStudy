alphabet = dict()
result = list()

for elem in list(input().upper()):
    if elem in alphabet:
        alphabet[elem] += 1
    else:
        alphabet[elem] = 1

for elem in zip(alphabet.keys(), alphabet.values()):
    # 횟수, 알파벳 순으로 넣기
    result.append((elem[1], elem[0]))

result.sort(reverse=True)

for elem1, elem2 in zip(result[:], result[1:]):
    if elem1[0] == elem2[0]:
        print("?")
        break
    else:
        print(result[0][1])
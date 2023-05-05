# 문제링크: https://softeer.ai/practice/info.do?idx=1&eid=990&sw_prbl_sbms_sn=180296

result = 0

for _ in range(5):
    start, end = input().split()
    startHour, startMin = int(start[:2]), int(start[3:])
    endHour, endMin = int(end[:2]), int(end[3:])

    if endMin >= startMin:
        tempHour = endHour - startHour
        tempMin = endMin - startMin
    elif endMin < startMin:
        tempHour = endHour - startHour - 1
        tempMin = 60 - (startMin - endMin)

    tempHour *= 60
    result += tempHour + tempMin

print(result)
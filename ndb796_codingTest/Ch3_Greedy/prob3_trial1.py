numList = [int(i) for i in input()]

while len(numList) >= 2:
    op1, op2 = numList.pop(), numList.pop()
    numList.insert(0,max(op1 + op2, op1 * op2))

print(numList[0])
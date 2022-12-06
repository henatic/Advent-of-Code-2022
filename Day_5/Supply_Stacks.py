from collections import deque

stack1 = deque()
stack2 = deque()
stack3 = deque()
stack4 = deque()
stack5 = deque()
stack6 = deque()
stack7 = deque()
stack8 = deque()
stack9 = deque()

doubleStack1 = deque()
doubleStack2 = deque()
doubleStack3 = deque()
doubleStack4 = deque()
doubleStack5 = deque()
doubleStack6 = deque()
doubleStack7 = deque()
doubleStack8 = deque()
doubleStack9 = deque()

def appendLeftStack(stack, val):
    if stack == 1:
        stack1.appendleft(val)
        doubleStack1.appendleft(val)
    elif stack == 2:
        stack2.appendleft(val)
        doubleStack2.appendleft(val)
    elif stack == 3:
        stack3.appendleft(val)
        doubleStack3.appendleft(val)
    elif stack == 4:
        stack4.appendleft(val)
        doubleStack4.appendleft(val)
    elif stack == 5:
        stack5.appendleft(val)
        doubleStack5.appendleft(val)
    elif stack == 6:
        stack6.append(val)
        doubleStack6.appendleft(val)
    elif stack == 7:
        stack7.appendleft(val)
        doubleStack7.appendleft(val)
    elif stack == 8:
        stack8.appendleft(val)
        doubleStack8.appendleft(val)
    else:
        stack9.appendleft(val)
        doubleStack9.appendleft(val)

def moveStacks(numStacks, fromSt, toSt):
    while numStacks > 0:
        popped = ''
        if fromSt == 1:
            popped = stack1.pop()
        elif fromSt == 2:
            popped = stack2.pop()
        elif fromSt == 3:
            popped = stack3.pop()
        elif fromSt == 4:
            popped = stack4.pop()
        elif fromSt == 5:
            popped = stack5.pop()
        elif fromSt == 6:
            popped = stack6.pop()
        elif fromSt == 7:
            popped = stack7.pop()
        elif fromSt == 8:
            popped = stack8.pop()
        else:
            popped = stack9.pop()
        
        if toSt == 1:
            stack1.append(popped)
        elif toSt == 2:
            stack2.append(popped)
        elif toSt == 3:
            stack3.append(popped)
        elif toSt == 4:
            stack4.append(popped)
        elif toSt == 5:
            stack5.append(popped)
        elif toSt == 6:
            stack6.append(popped)
        elif toSt == 7:
            stack7.append(popped)
        elif toSt == 8:
            stack8.append(popped)
        else:
            stack9.append(popped)

        numStacks -= 1

def moveMultiStack(numStacks, fromSt, toSt):
    temp = deque()
    while numStacks > 0:
        if fromSt == 1:
            temp.append(doubleStack1.pop())
        elif fromSt == 2:
            temp.append(doubleStack2.pop())
        elif fromSt == 3:
            temp.append(doubleStack3.pop())
        elif fromSt == 4:
            temp.append(doubleStack4.pop())
        elif fromSt == 5:
            temp.append(doubleStack5.pop())
        elif fromSt == 6:
            temp.append(doubleStack6.pop())
        elif fromSt == 7:
            temp.append(doubleStack7.pop())
        elif fromSt == 8:
            temp.append(doubleStack8.pop())
        else:
            temp.append(doubleStack9.pop())
        numStacks -= 1
    while len(temp) > 0:
        if toSt == 1:
            doubleStack1.append(temp.pop())
        elif toSt == 2:
            doubleStack2.append(temp.pop())
        elif toSt == 3:
            doubleStack3.append(temp.pop())
        elif toSt == 4:
            doubleStack4.append(temp.pop())
        elif toSt == 5:
            doubleStack5.append(temp.pop())
        elif toSt == 6:
            doubleStack6.append(temp.pop())
        elif toSt == 7:
            doubleStack7.append(temp.pop())
        elif toSt == 8:
            doubleStack8.append(temp.pop())
        else:
            doubleStack9.append(temp.pop())


f = open("input.txt", "r")

for x in f:
    line = x.strip()

    i = 0

    if line.find("[") != -1:
        stackNum = 1
        while i < len(line):
            if line[i] == '[':
                appendLeftStack(stackNum, line[i + 1])
            i += 4
            stackNum += 1
    elif line.find("m") != -1:
        i = 5
        numMove = ''
        while line[i] != " ":
            numMove += line[i]
            i += 1
        fromStack = int(line[i + 6])
        toStack = int(line[i + 11])
        moveStacks(int(numMove), fromStack, toStack)
        moveMultiStack(int(numMove), fromStack, toStack)
    

print("Our top stacks using CrateMover 9000: " + stack1[-1]+stack2[-1]+stack3[-1]+stack4[-1]+stack5[-1]+stack6[-1]+stack7[-1]+stack8[-1]+stack9[-1])
print("Our top stacks using CrateMover 9001: " + doubleStack1[-1]+doubleStack2[-1]+doubleStack3[-1]+doubleStack4[-1]+doubleStack5[-1]+doubleStack6[-1]+doubleStack7[-1]+doubleStack8[-1]+doubleStack9[-1])

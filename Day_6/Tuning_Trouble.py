f = open("input.txt", "r")

datastream = f.readline().strip()

charList = [datastream[0], datastream[1], datastream[2], datastream[3]]

i = 4

while i < len(datastream):
    if charList[0] == charList[1] or charList[0] == charList[2] or charList[0] == charList[3] or charList[1] == charList[2] or charList[1] == charList[3] or charList[2] == charList[3]:
        charList.remove(charList[0])
        charList.append(datastream[i])
        i += 1
    else:
        break

if i >= len(datastream):
    print("No start of packet.")
    exit(1)
else:
    print("Start of packet is at " + str(i) + ".\n" + str(charList))

msgString = ''
while len(msgString) < 14:
    msgString += datastream[i]
    i += 1

while i < len(datastream):
    iter = 0
    uniqueChars = False
    while iter < len(msgString) - 1:
        char = iter + 1
        while char < len(msgString) and uniqueChars == False:
            if msgString[iter] == msgString[char]:
                uniqueChars = True
            char += 1
        iter += 1
    if uniqueChars == False:
        break
    msgString = msgString[1:] + datastream[i]
    i += 1

if i >= len(datastream):
    print("No start of message.")
    exit(1)
else:
    print("Start of message is at " + str(i) + ".\n" + str(msgString))
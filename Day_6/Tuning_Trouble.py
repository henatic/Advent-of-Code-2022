# Open input file.
f = open("input.txt", "r")

# There's only one line to read, so we get the first line and strip away any potential "\n".
datastream = f.readline().strip()

# Part 1.

# List to hold the first 4 characters and update as we iterate though the packet.
charList = [datastream[0], datastream[1], datastream[2], datastream[3]]

# We start at index 4, because we already have characters from indexes 0 - 3.
i = 4

# Loop until our list has 4 unique characters, or until we hit the end of the input packet.
while i < len(datastream):

    # Test if any characters are identical to each other.
    if charList[0] == charList[1] or charList[0] == charList[2] or charList[0] == charList[3] or charList[1] == charList[2] or charList[1] == charList[3] or charList[2] == charList[3]:
        
        # If so, update our character list.
        charList.remove(charList[0])
        charList.append(datastream[i])
        i += 1

    # Otherwise, all 4 characters in our list are unique to each other.  We hope to get here.
    else:
        # Break from our while loop.
        break

# If our index variable is the string length, our code failed to find the start of the packet.
if i >= len(datastream):
    print("No start of packet.")

    # End our program.
    exit(1)

# Otherwise, we print our results for Part 1.
else:
    print("Start of packet is at " + str(i) + ".\n" + str(charList))

# Part 2.

# Initialize variable to hold the characters that should hopefully hold our start of the message.
msgString = ''

# Get the next 14 characters from the start of our packet, and append to our message string.
while len(msgString) < 14:
    msgString += datastream[i]
    i += 1

# Iterate through our packet until we get 14 unique characters.
while i < len(datastream):
    iter = 0
    noUnique = False
    while iter < len(msgString) - 1:
        char = iter + 1
        while char < len(msgString) and noUnique == False:
            if msgString[iter] == msgString[char]:
                noUnique = True
            char += 1
        iter += 1
    if noUnique == False:
        break
    msgString = msgString[1:] + datastream[i]
    i += 1

if i >= len(datastream):
    print("No start of message.")
    exit(1)
else:
    print("Start of message is at " + str(i) + ".\n" + str(msgString))
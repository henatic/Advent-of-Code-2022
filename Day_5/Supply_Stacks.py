from collections import deque

# Initialize stacks for Part 1.
stack1 = deque()
stack2 = deque()
stack3 = deque()
stack4 = deque()
stack5 = deque()
stack6 = deque()
stack7 = deque()
stack8 = deque()
stack9 = deque()

# initialize stacks for Part 2.
doubleStack1 = deque()
doubleStack2 = deque()
doubleStack3 = deque()
doubleStack4 = deque()
doubleStack5 = deque()
doubleStack6 = deque()
doubleStack7 = deque()
doubleStack8 = deque()
doubleStack9 = deque()

# Function to get the crates that need to be moved.
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

# Function for part 1 to move one crate at a time.
def moveStacks(numStacks, fromSt, toSt):

    # Moves crates from one stack to another accordingly.
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

# Function for part 2 to move more than one crate at a time.
def moveMultiStack(numStacks, fromSt, toSt):

    # Temporary deque structure to hold our crates in order.
    temp = deque()

    # Pop from selected stacks and append to temporary deque.
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
    
    # Add our crates in order into the indicated stack.
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

# Open the file stream to read the contents.
f = open("input.txt", "r")

# Read input file lines to gather the info we need and perform operations.
for x in f:
    # Remove potential "\n".
    line = x.strip()

    # Initialize index to 0.
    i = 0

    # An opening bracket indicates that we're reading the current state of the stacks.
    if line.find("[") != -1:

        # Indicates which stack we're reading.
        stackNum = 1

        # Read line to get crate and stack info.
        while i < len(line):

            # If line at index i contains an opening bracket, we found a crate in stack.
            if line[i] == '[':

                # Add stack info to our stack variables.
                appendLeftStack(stackNum, line[i + 1])

            # Increment by 4, because the format of the input involves a bracket every 4 spaces.
            i += 4

            # Go to next stack value.
            stackNum += 1

    # Otherwise, 'm' is how we indicate that we're reading an instruction to move crates.
    elif line.find("m") != -1:

        # Number of crates to move starts at index 5.
        i = 5

        # Initialize empty string to get number of crates to move.
        numMove = ''

        # Read until we hit a whitespace.
        while line[i] != " ":
            numMove += line[i]
            i += 1

        # Variables to hold stack number in integer form.
        fromStack = int(line[i + 6])
        toStack = int(line[i + 11])

        # Call move stack functions for parts 1 and 2.
        moveStacks(int(numMove), fromStack, toStack)
        moveMultiStack(int(numMove), fromStack, toStack)
    
# Print the results for our stacks.
print("Our top stacks using CrateMover 9000: " + stack1[-1]+stack2[-1]+stack3[-1]+stack4[-1]+stack5[-1]+stack6[-1]+stack7[-1]+stack8[-1]+stack9[-1])
print("Our top stacks using CrateMover 9001: " + doubleStack1[-1]+doubleStack2[-1]+doubleStack3[-1]+doubleStack4[-1]+doubleStack5[-1]+doubleStack6[-1]+doubleStack7[-1]+doubleStack8[-1]+doubleStack9[-1])

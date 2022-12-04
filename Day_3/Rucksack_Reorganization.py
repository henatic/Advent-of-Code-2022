import math

# Array of Letters.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "y", "z"]

# Create dictionary object to hold all cooresponding letters to their priorities.
priorities = dict()
priorityLow = 1
priorityHigh = 27

# Dynamically create priorities.
for letter in letters:
    priorities[letter] = priorityLow
    priorities[letter.upper()] = priorityHigh
    priorityLow += 1
    priorityHigh += 1

# Open file stream and initialize prioritySum.
f = open("input.txt", "r")
prioritySum = 0

# Begin iterating every line in the input file.
for x in f:

    # Get rid of default appended "\n".
    noNewLine = x.strip()

    # Grab the two halves of the input.
    compartment1 = x[0:math.trunc(len(noNewLine) / 2)]
    compartment2 = x[math.trunc(len(noNewLine) / 2):len(noNewLine)]

    itemType = list()

    # Store first half of values into first array.
    for item in compartment1:
        if item in compartment2 and item not in itemType:
            itemType.append(item)
            prioritySum += priorities[item]

print("Sum of priorities: " + str(prioritySum))
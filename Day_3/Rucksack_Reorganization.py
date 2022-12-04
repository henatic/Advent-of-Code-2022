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

# Initialization values for Part 2.
elfNum = 1
prioritySumGrouped = 0
commonItems = []
secondCommon = []
finalCommon = []

# Begin iterating every line in the input file.
for x in f:

    # Get rid of default appended "\n".
    noNewLine = x.strip()

    # For part 2, find the common item type for each group of three elves.
    # First elf gets a list of its items.
    if elfNum == 1:
        for item in noNewLine:
            if item not in commonItems:
                commonItems.append(item)
        
        # Increment to second elf for next iteration.
        elfNum += 1
    else:
        # Second elf gets a list of what items occurred in the first elf's racksack.
        if elfNum == 2:
            for item in commonItems:
                if item in noNewLine:
                    secondCommon.append(item)
            
            # Increment to third elf for next iteration.
            elfNum += 1
        
        # Third elf gets the final item(s) that occurred in the second elf's racksack.
        elif elfNum >= 3:
            for item in secondCommon:
                if item in noNewLine:
                    finalCommon.append(item)

            # Reset to first elf for next iteration.
            elfNum = 1

            # Increment the priority sum based on the three elves' item type.
            prioritySumGrouped += priorities[finalCommon[0]]

            # Clear lists for next group of elves.
            finalCommon.clear()
            secondCommon.clear()
            commonItems.clear()

    # Grab the two halves of the input.
    compartment1 = x[0:math.trunc(len(noNewLine) / 2)]
    compartment2 = x[math.trunc(len(noNewLine) / 2):len(noNewLine)]

    # List holds what item types were found for each rucksack.
    # We do this because we only want to add the priority to the sum only once for each common item found.
    itemType = list()

    # Check for common values .
    for item in compartment1:
        if item in compartment2 and item not in itemType:
            itemType.append(item)
            prioritySum += priorities[item]

print("Sum of priorities: " + str(prioritySum))
print("Sum of grouped priorities: " + str(prioritySumGrouped))
# Open input file to read inputs from.
f = open("input.txt", "r")

# Initialize the number of completely contained ranges.
numContain = 0
numOverlap = 0

# Iterate to find how many ranges have been contained.
for x in f:
    # Get rid of potential "\n".
    line = x.strip()

    # Begin separating input ranges by finding the separating comma.
    comma = line.find(",")

    # If no comma is found, exit the program.
    if comma == -1:
        print("Comma wasn't found in the line '" + line + "'.")
        exit(-1)
    
    # Set number range text to range values.
    range1 = line[0:comma]
    range2 = line[comma + 1:]

    # Find range dash to get numbers.
    dash1 = range1.find("-")
    dash2 = range2.find("-")

    # If not dash is found, exit the program.
    if range1 == -1 or range2 == -1:
        print("Dash wasn't found in the line '" + line + "'.")
        exit(1)

    # Determines if one range of numbers is contained within the other.
    # If so, we increment the number of contained set of ranges.
    if (int(range1[0:dash1]) >= int(range2[0:dash2]) and int(range1[dash1 + 1:]) <= int(range2[dash2 + 1:])) or (int(range1[0:dash1]) <= int(range2[0:dash2]) and int(range1[dash1 + 1:]) >= int(range2[dash2 + 1:])):
        numContain += 1
        numOverlap += 1

    # If not, we determine if the ranges overlap at all.
    # If so, we increment the number of overlapping set of ranges.
    elif (int(range1[0:dash1]) <= int(range2[dash2 + 1:]) and int(range1[0:dash1]) >= int(range2[0:dash2])) or (int(range1[dash1 + 1:]) <= int(range2[dash2 + 1:]) and int(range1[dash1 + 1:]) >= int(range2[0:dash2])):
        numOverlap += 1

# Print final results.
print("Number of contained assignments: " + str(numContain))
print("Number of overlapping assignments: " + str(numOverlap))
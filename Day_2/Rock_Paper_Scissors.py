f = open("input.txt", "r")

# Variables for the two parts of the daily puzzle.
totalScoreP1 = 0
totalScoreP2 = 0

scoreGuide = {
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3 # Scissors
}
outcomeGuide = {
    "Win": 6,
    "Tie": 3,
    "Lost": 0
}

def getChoice(opponent, outcome):
    if opponent == 'A':
        if outcome == 'Lost':
            return outcomeGuide[outcome] + scoreGuide["Z"]
        elif outcome == 'Tie':
            return outcomeGuide[outcome] + scoreGuide["X"]
        elif outcome == 'Win':
            return outcomeGuide[outcome] + scoreGuide["Y"]
    elif opponent == 'B':
        if outcome == 'Lost':
            return outcomeGuide[outcome] + scoreGuide["X"]
        elif outcome == 'Tie':
            return outcomeGuide[outcome] + scoreGuide["Y"]
        elif outcome == 'Win':
            return outcomeGuide[outcome] + scoreGuide["Z"]
    elif opponent == 'C':
        if outcome == 'Lost':
            return outcomeGuide[outcome] + scoreGuide["Y"]
        elif outcome == 'Tie':
            return outcomeGuide[outcome] + scoreGuide["Z"]
        elif outcome == 'Win':
            return outcomeGuide[outcome] + scoreGuide["X"]
    return 0


for x in f:

    # Statements for Part 1.
    if (x[0] == "A" and x[2] == "Y") or (x[0] == "B" and x[2] == "Z") or (x[0] == "C" and x[2] == "X"):
        totalScoreP1 += outcomeGuide['Win'] + scoreGuide[x[2]]
    elif (x[0] == "A" and x[2] == "X") or (x[0] == "B" and x[2] == "Y") or (x[0] == "C" and x[2] == "Z"):
        totalScoreP1 += outcomeGuide['Tie'] + scoreGuide[x[2]]
    else:
        totalScoreP1 += outcomeGuide['Lost'] + scoreGuide[x[2]]

    # Statements for Part 2.
    if(x[2] == "X"):
        totalScoreP2 += getChoice(x[0], "Lost")
    elif(x[2] == "Y"):
        totalScoreP2 += getChoice(x[0], "Tie")
    elif(x[2] == "Z"):
        totalScoreP2 += getChoice(x[0], "Win")

print("Part 1 Total Score: " + str(totalScoreP1))
print("Part 2 Total Score: " + str(totalScoreP2))
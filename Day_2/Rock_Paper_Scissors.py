f = open("input.txt", "r")
totalScore = 0
scoreGuide = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
outcomeGuide = {
    "Win": 6,
    "Tie": 3,
    "Lost": 0
}


for x in f:
    if (x[0] == "A" and x[2] == "Y") or (x[0] == "B" and x[2] == "Z") or (x[0] == "C" and x[2] == "X"):
        totalScore += outcomeGuide['Win'] + scoreGuide[x[2]]
    elif (x[0] == "A" and x[2] == "X") or (x[0] == "B" and x[2] == "Y") or (x[0] == "C" and x[2] == "Z"):
        totalScore += outcomeGuide['Tie'] + scoreGuide[x[2]]
    else:
        totalScore += outcomeGuide['Lost'] + scoreGuide[x[2]]

print("Total Score: " + str(totalScore))
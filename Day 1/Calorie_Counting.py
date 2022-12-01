f = open("input.txt", "r")
counter = 0
highestCalorieCount = 0
mostThreeCal = []

for x in f:
    if x.strip() == "":
        highestCalorieCount = max(highestCalorieCount, counter)
        mostThreeCal.append(counter)
        counter = 0
    else:
        counter += int(x)

highestCalorieCount = max(highestCalorieCount, counter)
mostThreeCal.append(counter)
mostThreeCal.sort(reverse=True)

print("Most calories: " + str(highestCalorieCount))
print("Highest three calories: " + str(mostThreeCal[0]) + " " + str(mostThreeCal[1]) + " " + str(mostThreeCal[2]))
print("Total of the three: " + str(mostThreeCal[0] + mostThreeCal[1] + mostThreeCal[2]))
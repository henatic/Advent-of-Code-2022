# Open input file.
f = open("input.txt", "r")

# Initialize scores and values for iterations.
counter = 0
highestCalorieCount = 0
mostThreeCal = []

# Calculate Calories.
for x in f:

    # Determine if we hit a blank line, representing the end of an elf's Calorie count.
    if x.strip() == "":

        # Record calories and highest calorie count.
        highestCalorieCount = max(highestCalorieCount, counter)
        mostThreeCal.append(counter)

        # Reset Calorie counter to 0 for next elf.
        counter = 0
    else:
        # Increment by number of Calories.
        counter += int(x)

# Input data doesn't end in blank line, so we keep record for the last elf.
highestCalorieCount = max(highestCalorieCount, counter)
mostThreeCal.append(counter)

# Sort list to get top 3 Calorie counts.
mostThreeCal.sort(reverse=True)

# Print final results.
print("Most calories: " + str(highestCalorieCount))
print("Highest three calories: " + str(mostThreeCal[0]) + " " + str(mostThreeCal[1]) + " " + str(mostThreeCal[2]))
print("Total of the three: " + str(mostThreeCal[0] + mostThreeCal[1] + mostThreeCal[2]))
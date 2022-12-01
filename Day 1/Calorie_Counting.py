f = open("input.txt", "r")
counter = 0
highestCalorieCount = 0
mostThreeCal = []

for x in f:
    if x.strip() == "":
        highestCalorieCount = max(highestCalorieCount, counter)
        if len(mostThreeCal) < 3:
            mostThreeCal.append(counter)
        elif mostThreeCal[0] < counter:
            mostThreeCal[0] = counter
        elif mostThreeCal[1] < counter:
            mostThreeCal[1] = counter
        elif mostThreeCal[2] < counter:
            mostThreeCal[2] = counter
        counter = 0
    else:
        counter += int(x)

highestCalorieCount = max(highestCalorieCount, counter)
if len(mostThreeCal) < 3:
    mostThreeCal.append(counter)
elif mostThreeCal[0] < counter:
    mostThreeCal[0] = counter
elif mostThreeCal[1] < counter:
    mostThreeCal[1] = counter
elif mostThreeCal[2] < counter:
    mostThreeCal[2] = counter

print(highestCalorieCount)
print(mostThreeCal)
print(mostThreeCal[0] + mostThreeCal[1] + mostThreeCal[2])
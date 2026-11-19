# Part 1 - Quiz Score Summary

passed = 0
total = 0
for score_number in range(1, 5):
    score = float(input(f"Score {score_number}: "))

    if score >= 60:
        print("Pass")
        passed = passed + 1
    else:
        print("Fail")
    total = total + score

average = total / 4

print("passed ", passed)
print("average ", average)

#Part 2 - Savings Goal tracker

goal = float(input(" Savings Goal: "))

while goal <= 0:
    print("Invalid goal")
    goal = float(input(" Savings Goal: "))

saved = 0
deposits = 0

while saved < goal:
    deposit = float(input(" Deposit: "))
    if deposit <= 0:
        print("Invalid deposit")
        continue
    saved = saved + deposit
    deposits = deposits + 1

    print("Saved so far: ", saved)

print("Goal reached!")
print("Saving goal: ", goal)
print("Final saved total: ", saved)
print("Accepted deposits: ", deposits)
print("Above goal: ", saved - goal)



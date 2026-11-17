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

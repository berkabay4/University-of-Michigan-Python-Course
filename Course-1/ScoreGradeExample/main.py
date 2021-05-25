# Take score value from user
score = input("Enter Score: ")

# Is this input are numeric input ?
try:
    fscore = float(score)

except:
    print("Error, please enter numeric input.")

if fscore <= 1.0 and fscore >= 0.9:
    sGrade = "A"

elif fscore < 0.9 and fscore >= 0.8:
    sGrade = "B"

elif fscore < 0.8 and fscore >= 0.7:
    sGrade = "C"

elif fscore < 0.7 and fscore >= 0.6:
    sGrade = "D"

else:
    sGrade = "F"

# Print grade of score,
print(sGrade)
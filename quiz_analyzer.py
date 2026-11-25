scores = []

for i in range(5):
    score = int(input(f"Enter Quiz {i + 1} score: "))
    scores.append(score)

print("\n==== QUIZ SCORE REPORT ====")
print(f"Quiz Scores: {scores}")

total_quizzes = len(scores)
print("Number of Quizzes:", total_quizzes)

total_score = sum(scores)
print("Total Score:", total_score)

avg = total_score / total_quizzes
print(f"Average Score: {avg:.2f}")

highest = max(scores)
print("Highest Score:", highest)

lowest = min(scores)
print("Lowest Score:", lowest)

ascending = sorted(scores)
print("Ascending:", ascending)

descending = sorted(scores, reverse = True)
print("Descending:", descending)

scores = []

print("===== JACKSTONES TOURNAMENT =====")

for i in range(5):
    score = int(input(f"Enter Score {i + 1}: "))

    while score < 0 or score > 10:
        print("Invalid score! Enter a score from 0 to 10.")
        score = int(input(f"Enter Score {i + 1}: "))

    scores.append(score)

backup = scores.copy()

print("\nOriginal Scores:", scores)
print("Backup successfully created.")

while True:
    print("\n===== JACKSTONES TOURNAMENT =====")
    print("[1] Display Scores")
    print("[2] Add Score")
    print("[3] Insert Score")
    print("[4] Remove Score")
    print("[5] Remove Last Score")
    print("[6] Search Score")
    print("[7] Generate Statistics")
    print("[8] Sort Scores")
    print("[9] Reverse Scores")
    print("[10] Clear Scores")
    print("[11] Restore Original Scores")
    print("[12] Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print("Current Scores:", scores)

    elif choice == 2:
        score = int(input("Enter score to add: "))

        if score >= 0 and score <= 10:
            scores.append(score)
            print("Updated Scores:", scores)
        else:
            print("Invalid score! Enter a score from 0 to 10.")

    elif choice == 3:
        index = int(input("Enter index: "))

        if index >= 0 and index <= len(scores):
            score = int(input("Enter score to insert: "))

            if score >= 0 and score <= 10:
                scores.insert(index, score)
                print("Updated Scores:", scores)
            else:
                print("Invalid score! Enter a score from 0 to 10.")
        else:
            print("Invalid index!")

    elif choice == 4:
        score = int(input("Enter score to remove: "))

        if score in scores:
            scores.remove(score)
            print("Updated Scores:", scores)
        else:
            print("Score not found!")

    elif choice == 5:
        if len(scores) > 0:
            removed = scores.pop()
            print("Removed Score:", removed)
            print("Updated Scores:", scores)
        else:
            print("The list is empty!")

    elif choice == 6:
        score = int(input("Enter score to search: "))
        count = scores.count(score)

        print("Number of Occurrences:", count)

        if count > 0:
            print("First Index:", scores.index(score))
        else:
            print("Score not found!")

    elif choice == 7:
        if len(scores) > 0:
            print("===== SCORE STATISTICS =====")
            print("Scores:", scores)
            print("Number of Scores:", len(scores))
            print("Total Score:", sum(scores))
            print("Average Score:", f"{sum(scores) / len(scores):.2f}")
            print("Highest Score:", max(scores))
            print("Lowest Score:", min(scores))
        else:
            print("No scores available!")

    elif choice == 8:
        if len(scores) > 0:
            print("[A] Ascending")
            print("[D] Descending")

            order = input("Enter sorting order: ").upper()

            if order == "A":
                scores.sort()
                print("Sorted Scores:", scores)
            elif order == "D":
                scores.sort(reverse=True)
                print("Sorted Scores:", scores)
            else:
                print("Invalid sorting order!")
        else:
            print("No scores available!")

    elif choice == 9:
        scores.reverse()
        print("Reversed Scores:", scores)

    elif choice == 10:
        scores.clear()
        print("All scores have been cleared.")
        print("Current Scores:", scores)

    elif choice == 11:
        scores = backup.copy()
        print("Original scores successfully restored.")
        print("Current Scores:", scores)

    elif choice == 12:
        print("Thank you for using the system!")
        break

    else:
        print("Invalid menu choice!")
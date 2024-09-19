task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        print(f"{task} is a high priority task", end="")
        if time_bound == "yes":
            print(" that requires immediate attention today!")
        else:
            print(" do it when you have time")
    case "medium":
        print(f"{task} is medium priority task", end="")
        if time_bound == "yes":
            print(" that needs to be done as soon as possible")
        else:
            print(" that can de done later")
    case "low":
        print(f"{task} is a low priority task", end="")
        if time_bound == "yes":
            print(" that needs to be done soon")
        else:
            print(". Consider completing it when you have free time")
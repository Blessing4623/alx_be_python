task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention")
        else:
            print(f"Note: '{task}' is a high priority task that need to be done")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that needs to be done as soon as possible")
        else:
            print(f"Note: '{task}' is a medium priority task that can be done later")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that can be done soon")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time")
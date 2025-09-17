# daily_reminder.py

# Demander la tâche
task = input("Enter your task: ")

# Demander la priorité
priority = input("Priority (high/medium/low): ").lower()

# Demander si la tâche est time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Construire le message de base selon la priorité
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unspecified priority"

# Ajouter la précision selon si la tâche est time-bound
if time_bound == "yes":
    final_message = base_message + " that requires immediate attention today!"
else:
    final_message = "Note: " + base_message + ". Consider completing it when you have free time."

# Afficher le rappel final
print("Reminder:", final_message)

def add_task():
    """Prompt the user for a task and append it to the list."""
    task = input("\nEnter a new task: ").strip()
    if task:                         # don't add empty strings
        tasks.append(task)           # ← the core skill: list.append()
        print(f'  ✔  "{task}" added!')
    else:
        print("  ✘  Task cannot be empty.")


def view_tasks():
    """Print every task with its position number."""
    print("\n─── Your Tasks ───────────────────────")
    if not tasks:                    # handle an empty list gracefully
        print("  (no tasks yet — add one!)")
    else:
        for index, task in enumerate(tasks, start=1):   # ← loop skill
            print(f"  {index}. {task}")
    print("──────────────────────────────────────")


def delete_task():
    """Remove a task by its number."""
    view_tasks()
    if not tasks:
        return
    try:
        number = int(input("Enter the task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)   # pop() removes by index
            print(f'  ✔  "{removed}" removed.')
        else:
            print("  ✘  That number is out of range.")
    except ValueError:
        print("  ✘  Please enter a valid number.")


def show_menu():
    """Display the main menu."""
    print("\n╔══════════════════════════╗")
    print("║      TASK  MANAGER       ║")
    print("╠══════════════════════════╣")
    print("║  1. Add a task           ║")
    print("║  2. View all tasks       ║")
    print("║  3. Delete a task        ║")
    print("║  4. Quit                 ║")
    print("╚══════════════════════════╝")


# ---------- MAIN LOOP ----------

def main():
    print("\nWelcome to Task Manager!")
    print("(This program stores your tasks in a Python list.)\n")

    while True:                          # keep running until the user quits
        show_menu()
        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("\nGoodbye! Tasks are cleared when the program closes.")
            print("(Saving to a file is the next challenge!)\n")
            break
        else:
            print("  ✘  Invalid option. Please choose 1, 2, 3, or 4.")


# ---------- ENTRY POINT ----------
if __name__ == "__main__":
    main()
# Building a CLI TO-DO List Application in Python

# Define a function that welcomes the user and displays the menu options
def display_menu():  
    print("\nWelcome to your TO-DO List. Please choose an option from the menu.")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Quit")

# Define a function that adds a new task to the TO-DO List    
def add_task(tasks):
    task = input("Enter the task:")  # create a variable for task input
    tasks.append(task)   # Adds tasks to the task list
    print("Task added successfully!") # Prints a successfully added statement
    
# Define a function to display the tasks in the TO-DO List    
def view_tasks(tasks):    
    if not tasks:  
        print("No tasks in TO-DO List") # This will print if there are no tasks in the list
    else:
        print("\nTasks:") # Prints if there are tasks in the TO-DO List    
        for i in range(len(tasks)): # A "for" loop that iterates through the length of the "tasks"list where "i" represents the index of each task in the list
            print(f"{i + 1}. {tasks[i]}")  # An f-string that adds 1 to the current index starting the numbering at 1 instead of 0, accessing the element at the current index in the list and concatenating the number with the task desription
            
# Defines a function to delete tasks from the list            
def delete_tasks(tasks):
    if not tasks:
        print("No tasks to delete.")
    else:
        view_tasks(tasks)    # Calls the view tasks function to display the list to choose which task to delete
        while True:  # Creates a loop that will continue until broken by break statement
            try:  # Error handling, the code will exectute in this block and jump to except block if an error is found
                choice = int(input("Enter the task number to delete:")) # Prompts the user to enter the number of the task they want to delete
                if 1 <= choice <= len(tasks):   # Checks to see if the number entered is within the valid range of tasks in the list
                    del tasks[choice - 1]     # If the choice is valid, this deletes the task at the specified index (remember the indices start at zero)
                    print("Task deleted successfully!")
                    break
                else:
                    print("Invalid task number. Please try again.")
            except ValueError:     # If the user enters something that can't be converted into an integer, this catches the error and prints an error message
                print("Invalid input. Please enter a number.")                        

# Main function to run the TO-DO List application
def main():             
    tasks = []    # Creates the empty list to hold the task elements
    while True: # Creates loop that runs until the user exits
        display_menu() # Calls the display menu function
        try:  # This block handles potential errors if the user enters an non- numeric number in the choice menu
            choice = int(input("Enter your choice:")) # The following execute different functions based on the users input
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                delete_tasks(tasks)
            elif choice == 4:
                print("Exiting TO-DO List...")
            else:
                print("Invalid choice. Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        input("\nPress Enter to continue...")
        
if __name__ == "__main__": # This line ensures that the "main" function is only executed when the script is run directly
    main()                             
    
      
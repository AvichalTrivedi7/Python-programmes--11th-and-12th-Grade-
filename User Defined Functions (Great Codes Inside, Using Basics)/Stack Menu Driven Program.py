stack = []  # Empty stack

def push(stack):
    item = input("Enter the item to push: ")
    stack.append(item)
    print(f"{item} pushed into the stack")

def pop(stack):
    if len(stack) == 0:
        print("Stack is empty! Nothing to pop.")
    else:
        item = stack.pop()
        print(f"{item} popped from the stack")

def display(stack):
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print("Stack elements:", stack)

ch = 'y'
while ch.lower() == 'y':
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        push(stack)
    elif choice == '2':
        pop(stack)
    elif choice == '3':
        display(stack)
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")

    ch = input("Do you want to continue? (y/n): ")

print("Program ended.")

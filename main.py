def get_todos():
    with open ('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add or show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        with open ('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = user_action[5:]
            number = int(number) - 1
            new_todo = input("Enter new todo: ")

            todos = get_todos()

            todos[number] = new_todo + '\n'

            with open ('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todo_to_remove = todos[number-1].strip('\n')
            todos.pop(number - 1)


            with open ('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no todo with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Please enter a valid input")

print("Goodbye!")
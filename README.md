# Todo App

A simple command-line todo app built with Python. It lets you add, view, edit, and complete todo items, storing them in a local `todos.txt` file.

## Features

- Add new todo items
- Show all saved todos
- Edit an existing todo
- Complete and remove a todo
- Save todos between runs using a text file
- Use helper functions to read and write todo data

## Requirements

- Python 3

No external packages are required.

## How to Run

From the project folder, run:

```bash
python cli.py
```

Depending on your system, you may need:

```bash
python3 cli.py
```

## Commands

Use these commands when the app asks for input:

```text
add Buy groceries
show
edit 1
complete 1
exit
```

## Example

```text
Type add or show, edit, complete or exit: add Learn Python
Type add or show, edit, complete or exit: show
1-Learn Python
Type add or show, edit, complete or exit: complete 1
Todo Learn Python was removed from the list.
Type add or show, edit, complete or exit: exit
Goodbye!
```

## Project Structure

```text
todo_app/
├── functions.py
├── main.py
├── todos.txt
└── README.md
```

## Notes

The app reads from and writes to `todos.txt`, so keep that file in the same folder as `main.py`.

`main.py` handles the command-line interaction, while `functions.py` contains the helper functions for reading from and writing to the todo file.

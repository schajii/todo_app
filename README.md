# Todo App

A simple Python todo app with two interfaces: a **command-line interface (CLI)** and a **graphical user interface (GUI)**. Todos are stored locally in a `todos.txt` file and persist between runs.

## Features

- Add new todo items
- View all saved todos
- Edit an existing todo
- Mark a todo as complete (removes it from the list)
- Live clock display in the GUI
- Persistent storage via `todos.txt`

## Requirements

- Python 3.14+
- [FreeSimpleGUI](https://github.com/spyoungtech/FreeSimpleGUI) (for the GUI)

Install dependencies using [uv](https://github.com/astral-sh/uv):

```bash
uv sync
```

Or with pip:

```bash
pip install freesimplegui
```

## How to Run

### GUI

```bash
python gui.py
```

### CLI

```bash
python cli.py
```

## CLI Commands

```text
add <todo>     Add a new todo item
show           List all todos with their numbers
edit <number>  Edit the todo at the given number
complete <n>   Remove the todo at the given number
exit           Quit the app
```

### Example

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
├── gui.py          # GUI interface (FreeSimpleGUI)
├── cli.py          # Command-line interface
├── functions.py    # Shared helpers for reading/writing todos.txt
├── todos.txt       # Persistent todo storage
├── pyproject.toml
└── README.md
```

## Notes

Both `gui.py` and `cli.py` share the same `functions.py` helpers and the same `todos.txt` file, so todos created in one interface are visible in the other.

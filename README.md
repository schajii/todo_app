# Todo App

A simple Python todo app with three ways to use it:

- **GUI** — desktop window built with [FreeSimpleGUI](https://github.com/spyoungtech/FreeSimpleGUI)
- **CLI** — interactive terminal interface
- **macOS app** — double-clickable `Todo.app` bundle

Todos are stored in a plain `todos.txt` file and persist between runs.

## Features

- Add, view, edit, and complete todo items
- Live clock in the GUI
- Shared read/write helpers in `functions.py`
- Automatic creation of `todos.txt` on first run

## Requirements

- Python 3.14+
- FreeSimpleGUI (GUI only)

Install dependencies with [uv](https://github.com/astral-sh/uv):

```bash
uv sync
```

Or with pip:

```bash
pip install freesimplegui
```

## How to Run

### GUI

From the project directory:

```bash
python gui.py
```

### CLI

```bash
python cli.py
```

### macOS App

Open `Todo.app` from Finder, or run:

```bash
open Todo.app
```

## CLI Usage

| Command | Description |
|---|---|
| `add <todo>` | Add a new todo |
| `show` | List all todos with numbers |
| `edit <number>` | Edit a todo by its number |
| `complete <number>` | Remove a todo by its number |
| `exit` | Quit the app |

Example session:

```text
Type add or show, edit, complete or exit: add Learn Python
Type add or show, edit, complete or exit: show
1-Learn Python
Type add or show, edit, complete or exit: complete 1
Todo Learn Python was removed from the list.
Type add or show, edit, complete or exit: exit
Goodbye!
```

## GUI Usage

1. Type a todo in the input box and click **Add**.
2. Select a todo in the list to load it into the input box.
3. Change the text and click **Edit** to update the selected item.
4. Select a todo and click **Complete** to remove it.
5. Click **Exit** or close the window to quit.

## Data Storage

`functions.py` stores todos in a file next to itself:

```python
BASEDIR = os.path.dirname(os.path.abspath(__file__))
FILEPATH = os.path.join(BASEDIR, "todos.txt")
```

That keeps file paths reliable regardless of the current working directory — important when the app is launched as a macOS bundle.

| How you run the app | Where todos are saved |
|---|---|
| `python gui.py` or `python cli.py` | `./todos.txt` (project root) |
| `Todo.app` | `Todo.app/Contents/Resources/todos.txt` |

The CLI and GUI share the same file when run from the project folder. The bundled macOS app uses its own copy inside the app bundle.

If you rebuild `Todo.app`, make sure the updated `functions.py` is included in the bundle.

## Project Structure

```text
todo_app/
├── gui.py              # GUI entry point
├── cli.py              # CLI entry point
├── functions.py        # Read/write helpers and file path logic
├── todos.txt           # Todo storage (created automatically)
├── Todo.app/           # macOS app bundle
│   └── Contents/
│       └── Resources/
│           ├── script        # Bundled GUI script
│           ├── functions.py  # Bundled helpers
│           └── todos.txt     # Todo storage for the app bundle
├── pyproject.toml
└── README.md
```

# Todo App

A simple Python todo app with four ways to use it:

- **CLI** — interactive terminal interface
- **GUI** — desktop window built with [FreeSimpleGUI](https://github.com/spyoungtech/FreeSimpleGUI)
- **Web** — browser interface built with [Streamlit](https://streamlit.io/)
- **macOS app** — double-clickable `Todo.app` bundle

Todos are stored in a plain `todos.txt` file and persist between runs.

## Features

- Add, view, edit, and complete todo items
- Live clock in the GUI
- Web interface with checkboxes to complete todos
- Shared read/write helpers in `functions.py`
- Automatic creation of `todos.txt` on first run

## Requirements

- Python 3.14+
- FreeSimpleGUI (GUI and macOS app)
- Streamlit (web interface)

Install dependencies with [uv](https://github.com/astral-sh/uv):

```bash
uv sync
```

Add a new package with uv:

```bash
uv add package-name
```

Or with pip:

```bash
pip install freesimplegui streamlit
```

## How to Run

Run commands from the project directory. With uv, you do not need to activate the virtual environment first.

### CLI

```bash
uv run python cli.py
```

### GUI

```bash
uv run python gui.py
```

### Web

```bash
uv run streamlit run web.py
```

Streamlit opens the app in your browser, usually at `http://localhost:8501`.

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

## Web Usage

1. Open the app with `uv run streamlit run web.py`.
2. Type a new todo in the input box at the bottom and press Enter to add it.
3. Check a todo's checkbox to mark it complete and remove it from the list.

## Data Storage

`functions.py` resolves the todo file path based on how the app is running:

- From the project folder, todos are saved next to `functions.py`.
- From the macOS app bundle, todos are saved in Application Support.

| How you run the app | Where todos are saved |
|---|---|
| `python cli.py`, `python gui.py`, or `streamlit run web.py` | `./todos.txt` (project root) |
| `Todo.app` | `~/Library/Application Support/Todo/todos.txt` |

The CLI, GUI, and web app share the same file when run from the project folder. The bundled macOS app uses its own storage location.

If you rebuild `Todo.app`, make sure the updated `functions.py` is included in the bundle.

## Project Structure

```text
todo_app/
├── cli.py              # CLI entry point
├── gui.py              # GUI entry point
├── web.py              # Streamlit web entry point
├── functions.py        # Read/write helpers and file path logic
├── todos.txt           # Todo storage (created automatically)
├── Todo.app/           # macOS app bundle
│   └── Contents/
│       └── Resources/
│           ├── script        # Bundled GUI script
│           ├── functions.py  # Bundled helpers
│           └── todos.txt     # Legacy todo storage (migrated on first run)
├── pyproject.toml
├── uv.lock
└── README.md
```

import os
import shutil


def _get_data_dir():
    """Use Application Support when running inside the macOS app bundle."""
    if ".app/Contents/Resources" in os.path.abspath(__file__):
        resources_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(
            os.path.expanduser("~"), "Library", "Application Support", "Todo"
        )
        os.makedirs(data_dir, exist_ok=True)

        new_file = os.path.join(data_dir, "todos.txt")
        old_file = os.path.join(resources_dir, "todos.txt")
        if not os.path.exists(new_file) and os.path.exists(old_file):
            shutil.copy2(old_file, new_file)

        return data_dir
    return os.path.dirname(os.path.abspath(__file__))


BASEDIR = _get_data_dir()
FILEPATH = os.path.join(BASEDIR, "todos.txt")


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file_local:
            pass
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

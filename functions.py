# Constant creation in python file with capital letters.
FILEPATH = "todos.txt"
# giving default value to filepath parameter


def get_todos(filepath=FILEPATH):
    # Opening a file and reading its already existing content as list using readlines.
    # using context manager format. No need to write file.close() when using 'with' context manager
    with open(filepath, 'r') as filer:
        todos_local = filer.readlines()
    return todos_local
# non-default parameter comes before default parameter


def write_todos(todos_local, filepath=FILEPATH):
    # overwrite the file with appended list
    with open(filepath, 'w') as filew:
        filew.writelines(todos_local)


if __name__ == "__main__":
    print("Functions file is running as main.")
    print(get_todos())
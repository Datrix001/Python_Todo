def file_read(filepath="todos.txt"):
    with open(filepath, "r") as local_file:
        local_todos = local_file.readlines()
    return local_todos


def file_write(local_todos, filepath="todos.txt"):
    with open(filepath, "w") as local_file:
        local_file.writelines(local_todos)
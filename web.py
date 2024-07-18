import os.path

import streamlit as st
import function

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

todos = function.file_read()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.file_write(todos)

def delete_todo():
    tod = st.session_state["i"]
    print(tod)
    todos.remove(tod)
    function.file_write(todos)



st.title("My todo App")
st.subheader("This is my todo app")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(f"{todo}", key=todo)
    if checkbox:
        todos.pop(index)
        function.file_write(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label=" ", placeholder="Add a new todo....", on_change=add_todo,
              key="new_todo")



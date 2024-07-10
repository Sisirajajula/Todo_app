import streamlit as st
import functions

todos = functions.get_todos()


# add new todos to todos list
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    print(todos)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")

# remove completed items from todos list
# only when widgets have key they appear in st.session_state
for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()


st.text_input(label="Add a new todo", placeholder="Add new todo",
              on_change=add_todo,
              key="new_todo")

# st.session_state : keeps track of all inputs
# from user in the form of dictionary

st.session_state

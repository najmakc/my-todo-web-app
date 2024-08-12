import streamlit as st
import functions
# Initialize todos from functions
todos = functions.get_todos()
print(todos)

# Define the add_todo function
def add_todo():
    todo=st.session_state["new_todo"]   #This is a dictionary , {"new_todo" :"Django"} , Access the value of "new_todo" from session state (a dictionary)
    todos.append(todo+"\n")        #Append the new to-do item to the list (with a newline character) ,- Modifying Global Variables: You don’t need global # if you’re just modifying the contents of a global variable. global is only needed if you are reassigning the variable.
    functions.write_todos(todos)    #Write the updated list back to text file
    # Clear the input field after adding the todo
    st.session_state["new_todo"]=""

# Set up the Streamlit app UI
st.title("My To do App")
st.subheader("This is my to do app")
st.write("This app is to increase your productivity")
# Display the current todos with checkboxes

#method 1
# for index, todo in enumerate(todos):
     # if todo.strip("\n"):  #it's checking the string is empty or not after removing the leading /ending "\n" if its empty it will not continue
     #    st.checkbox(todo, key=f"checkbox_{index}")

#method 2
for todo in todos:
    if todo.strip("\n"): #checks if the current to-do is not empty after removing leading/trailing newline characters. This ensures that only non-empty todos are processed.
        checkbox=st.checkbox(todo, key=todo) #Creates a checkbox for each to-do item. The key=todo ensures that each checkbox is uniquely identified by its corresponding to-do text.
        # print(checkbox) it print True/False

        #Removing a To-Do item
        if checkbox: #The value of checkbox is True if the checkbox is checked and False otherwise.
            #if checkbox: checks if the checkbox is checked (i.e., True), indicating the user wants to mark the task as completed.
            #todos.remove(todo) removes the selected todo from the todos list.
            #functions.write_todos(todos) writes the updated list of todos back to text file, effectively saving the new state after the removal.
            todos.remove(todo)
            functions.write_todos(todos)
            #del st.session_state[todo] deletes the corresponding key from st.session_state to clean up the session state and remove the key-value pair associated with the removed to-do.
            del st.session_state[todo] #using the del keyword, which is the most common method of removing a key-value pair from a dictionary
            #st.rerun() forces a rerun of the entire Streamlit script. This ensures the app updates immediately, reflecting the removal of the to-do item without the user needing to refresh the page manually.
            st.rerun()




# Add new todo to the list
st.text_input(label="" ,
              placeholder="Add a new todo" ,
              on_change=add_todo,    # Pass the function reference directly
              key="new_todo")
#on_change=add_todo specifies that the add_todo function should be called when the user submits a new to-do (i.e., when the input value changes).
#key="new_todo" associates the input field with a key in st.session_state, which allows the input to be accessed within add_todo().

#important notes

# Summary of Removing an Item from the List:
# When a checkbox is checked:
# The corresponding todo item is removed from the todos list using todos.remove(todo).
# The updated todos list is saved using functions.write_todos(todos).
# The key associated with that todo is deleted from st.session_state to keep the session state clean.
# st.rerun() triggers a full rerun of the app, which re-displays the list of to-dos without the removed item.
# This ensures the app dynamically updates, allowing users to add or remove to-dos seamlessly


# notes
# st.session_state
#st.session_state is a dictionary-like object that stores variables across Streamlit reruns.

# notes about streamlit
#
# In Streamlit, the on_change parameter is used with certain widgets to specify a callback function that should be called when the widget's value changes. This parameter allows you to execute a function in response to user interactions with the widget, such as when a user types into a text input field or changes the state of a checkbox.
#
# Understanding on_change
# Purpose:
#
# The on_change parameter provides a way to react to changes in the widget's state. When the value of the widget changes, Streamlit calls the function assigned to on_change.
# How It Works:
#
# When a user interacts with a widget that has an on_change parameter set, Streamlit triggers the specified callback function. This function can then perform operations or update the app state in response to the change.
# Usage:
#
# on_change should be set to a function reference (i.e., the function name without parentheses). Streamlit will call this function without any arguments when the widget's value changes.

#Program explanation
# In Streamlit, the app script is re-run from top to bottom every time a user interaction triggers a change, such as adding a new todo. This behavior ensures that your application always reflects the most current state of your data.
#
# Here’s how it works and how to ensure that the updated todo list is shown correctly:
#
# How Streamlit Reruns the Script
# User Interaction:
#
# When a user adds a new todo item and submits it (by typing in the input field and triggering the on_change function), Streamlit automatically reruns the entire script.
# Re-running the Script:
#
# During the rerun, Streamlit re-executes the script from the top. This means that all the code for setting up and displaying the todo list will be executed again, including the code that retrieves the updated list of todos.
# Displaying Updated List:
#
# Since the script is rerun, the updated todos list (which includes the newly added todo) will be used to render the updated list of checkboxes.
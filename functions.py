#Custom functions to read the file into a list
# FILEPATH=r"C:\Users\NAJMA K C\Downloads\Python Mega Course Learn Python in 60 Days, Build 20 Apps-20240804T173949Z-001\Python Mega Course Learn Python in 60 Days, Build 20 Apps\todos.txt"
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items"""
    with open(filepath,"r") as file_local:
            todos_local=file_local.readlines()
    return todos_local
# print(help(get_todos))

def write_todos(todos_arg,filepath=FILEPATH):
    """write the to-do items list in the text file """
    with open(filepath,"w") as file:
        file.writelines(todos_arg)

#here print(__name__) __name__ string variable and it will print name of function/file/ if we are exceuting this file only
#means functions.py running print(__name__) its output will be __main__
#if we arerunning functions.py from the main functions by import functions.py then print(__name__) its output will be
#functions.py at that time the main function will be the __main__
# print("hello dear manasi")
# print(__name__)
if __name__=="__main__":
     print("hey")
     print(get_todos())
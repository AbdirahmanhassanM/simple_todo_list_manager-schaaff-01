import sys
import datetime

def helper():
    """
    Help function.
    Instructions on how user can interact with todo list manager.
    """
    sa = """Usage :-
    $ ./todo add "todo item"  # Add a new todo
    $ ./todo show             # Show remaining todos
    $ ./todo del NUMBER       # Delete a todo
    $ ./todo done NUMBER      # Complete a todo
    $ ./todo helper           # Show usage"""
    sys.stdout.buffer.write(sa.encode('utf8'))


def add(todo: str):
    """
    function to add new todo to existing todo.txt file
    Args:
    todo (str): Description of a new todo
    """
    todo_file = open('todo.txt', 'a')
    todo_file.write(todo)
    todo_file.write("\n")
    todo_file.close()
    print(f'Added todo: "{todo}"')


def delete(todo_number):
    """
    function to delete items from the todo list
    Args:
    todo_number : todo id, which will be deleted
    """
    try:
        enumerate_todolist()
        with open("todo.txt", "r") as todo_file:
            lines = todo_file.readlines()
            todo_file.seek(0)
            for line in lines:
                if line.strip('\n') != todo_list_dict[int(todo_number)]:
                    todo_file.write(line)
            todo_file.truncate()
        print(f"Deleted todo #{todo_number}")

    except Exception as e:
        print(f"Error: todo #{todo_number} does not exist. No todo deleted.")


def done(todo_number):
    """
    function to mark todos as done on the todo list
    Args:
    todo_number : todo id, which will be marked as done
    """
    try:
        enumerate_todolist()
        done_file = open('done.txt', 'a')
        done_todo_entry = 'x '+str(datetime.datetime.today()).split()[0]+' '+todo_list_dict[int(todo_number)]
        done_file.write(done_todo_entry)
        done_file.write("\n")
        done_file.close()
        print(f"Marked todo #{todo_number} as done.")

        # delete done todo from todo list
        delete(todo_number)
    
    except:
        print(f"Error: todo #{todo_number} does not exist.")


def show():
    """
    Function to output current todo list
    """
    try:
        enumerate_todolist()
        
        for todo in range(len(todo_list_dict), 0, -1):
            sys.stdout.buffer.write(f"[{todo}] {todo_list_dict[todo]}".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
        
    except Exception as e:
        raise e


def enumerate_todolist():
    """
    Helper function.
    Updates dictionary of todos based on lines in todo.txt file.
    """
    try:
        todo_file = open('todo.txt', 'r')
        line_counter = 1
        for line in todo_file:
            line = line.sprip('\n')
            todo_list_dict.update({line_counter: line})
            line_counter += 1
    except:
        sys.stdout.buffer.write("There are no pending todos! :)".encode('utf8'))

if __name__ == '__main__':
    try:
        todo_list_dict = {}
        done_list_dict = {}
        args = sys.argv

        # change argument for delete for simple function call
        if (args[1] == 'del'):
            args[1] == 'delete'
        
        if (args[1] == 'add' and len(args[2:]) == 0):
            sys.stdout.buffer.write("Error: Missing content of todo. Nothing added.")

        elif (args[1] == 'del' and len(args[2:]) == 0):
            sys.stdout.buffer.write("Error: Todo number is missing. No todo deletet.")
        
        elif (args[1] == 'done' and len(args[2:]) == 0):
            sys.stdout.buffer.write("Error: Todo number is missing. No todo marked is done.")
        else:
            globals()[args[1]](*args[2:])

    except Exception as e:
        helper()
        
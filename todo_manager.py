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
    $ ./todo sort [order]     # Sort todos (alphabetical or date_created)
    $ ./todo helper           # Show usage"""
    sys.stdout.buffer.write(sa.encode('utf8'))


def add(todo: str):
    """
    Function to add a new todo to the existing todo.txt file.
    Args:
    todo (str): Description of a new todo.
    """
    todo_file = open('todo.txt', 'a')
    todo_file.write(todo)
    todo_file.write("\n")
    todo_file.close()
    print(f'Added todo: "{todo}"')


def delete(todo_number):
    """
    Function to delete items from the todo list.
    Args:
    todo_number : todo id, which will be deleted.
    """
    try:
        enumerate_todolist()
        with open("todo.txt", "r+") as todo_file:
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
    Function to mark todos as done on the todo list.
    Args:
    todo_number : todo id, which will be marked as done.
    """
    try:
        enumerate_todolist()
        with open('done.txt', 'a') as done_file:
            done_todo_entry = 'x '+str(datetime.datetime.today()).split()[0]+' '+todo_list_dict[int(todo_number)]
            done_file.write(done_todo_entry + "\n")
        print(f"Marked todo #{todo_number} as done.")

        # delete done todo from todo list
        delete(todo_number)
    
    except:
        print(f"Error: todo #{todo_number} does not exist.")


def show():
    """
    Function to output current todo list.
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
            line = line.strip('\n')
            todo_list_dict.update({line_counter: line})
            line_counter += 1
    except:
        sys.stdout.buffer.write("There are no pending todos! :)".encode('utf8'))


def sort_todos(order="alphabetical"):
    """
    Function to sort the todo list based on the specified order.
    Args:
    order (str): The sorting order - "alphabetical" or "date_created".
    """
    try:
        with open("todo.txt", "r") as todo_file:
            todos = [line.strip() for line in todo_file.readlines()]

        if not todos:
            print("There are no todos to sort!")
            return

        if order == "alphabetical":
            todos.sort()
        elif order == "date_created":
            todos.sort(key=lambda x: x.split()[0])  # Adjust for your date format
        else:
            print("Invalid sorting order. Use 'alphabetical' or 'date_created'.")
            return

        with open("todo.txt", "w") as todo_file:
            for todo in todos:
                todo_file.write(todo + "\n")

        print(f"Todos sorted by {order} successfully!")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    try:
        todo_list_dict = {}
        done_list_dict = {}
        args = sys.argv

        # change argument for delete for simple function call
        if (args[1] == 'del'):
            args[1] = 'delete'
        
        if (args[1] == 'add' and len(args[2:]) == 0):
            sys.stdout.buffer.write("Error: Missing content of todo. Nothing added.".encode('utf8'))

        elif (args[1] == 'del' and len(args[2:]) == 0):
            sys.stdout.buffer.write("Error: Todo number is missing. No todo deleted.".encode('utf8'))
        
        elif (args[1] == 'done' and len(args[2:]) == 0):
            sys.stdout.buffer.write("Error: Todo number is missing. No todo marked as done.".encode('utf8'))
        elif (args[1] == 'sort' and len(args[2:]) == 0):
            sort_todos()
        elif (args[1] == 'sort' and len(args[2:]) > 0):
            sort_todos(*args[2:])
        else:
            globals()[args[1]](*args[2:])

    except Exception as e:
        helper()

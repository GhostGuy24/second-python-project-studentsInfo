from students_operations import *

if __name__ == "__main__":
    user_selection = ""
    while True:
        user_selection = Actions(int(menu()))
        clear_terminal()

        if user_selection == Actions.EXIT: exit()
        elif user_selection == Actions.ADD: add_student()
        if user_selection == Actions.FIND:find_student()
        if user_selection == Actions.DELETE:delete_student()
        # if user_selection == Actions.UPDATE:
        elif user_selection == Actions.DISPLAY:display_students()

#main.py
from user_interface import UserInterface #importing user interface
from business_logic import BusinessLogic#importing the business logic


def main():
    ui = UserInterface()
    bl = BusinessLogic()
    """ presenting menu according to role else suggest that the role is invalid    
    """
    while True:
        role = ui.get_role()
        if role == "admin":
            ui.admin_menu(bl)
        elif role == "data_engineer":
            ui.data_engineer_menu(bl)
        elif role == "user":
            ui.user_menu(bl)
        else:
            print("Invalid role. Exiting.")
            break

if __name__ == "__main__":
    main()

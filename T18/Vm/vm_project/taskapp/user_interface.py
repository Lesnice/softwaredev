class UserInterface:
    def get_role(self):
        print("Select role: ")
        print("1. Admin")
        print("2. Data Engineer")
        print("3. User")
        choice = input("Enter role: ")
        role_mapping = {"1": "admin", "2": "data_engineer", "3": "user"}
        return role_mapping.get(choice, "invalid")

    def admin_menu(self, business_logic):
        print("Admin Menu")
        print("1. Create User")
        print("2. List Users")
        choice = input("Enter choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role: ")
            business_logic.create_user(username, password, role) #create user
        elif choice == "2":
            users = business_logic.list_users() #list all users
            for user in users:
                print(user)
        else:
            print("Invalid choice.")

    def data_engineer_menu(self, business_logic):
        print("Data Engineer Menu")
        print("1. Run Custom SQL Query")
        print("2. Run Data Pipeline")
        choice = input("Enter choice: ")
        if choice == "1":
            query = input("Enter SQL query: ")
            try:
                result = business_logic.execute_query(query) #execute custom SQL query
                for row in result:
                    print(row)
            except Exception as e:
                print(f"Error executing query: {e}")
        elif choice == "2":
            business_logic.run_data_pipeline() #Run data pipeline
        else:
            print("Invalid choice.")

    def user_menu(self, business_logic):
        print("User Menu")
        print("1. Add Data")
        print("2. Read Data")
        print("3. Update Data")
        print("4. Delete Data")
        choice = input("Enter choice: ")
        if choice == "1":
            content = input("Enter data content: ")
            business_logic.add_data(content)
        elif choice == "2":
            data_id = input("Enter data ID to read: ")
            data = business_logic.read_data(data_id) #read data
            if data:
                print(data)
            else:
                print("Data not found.")
        elif choice == "3":
            data_id = input("Enter data ID to update: ")
            new_content = input("Enter new data content: ") #update data by ID
            business_logic.update_data(data_id, new_content)
        elif choice == "4":
            data_id = input("Enter data ID to delete: ")
            business_logic.delete_data(data_id) #delete data by ID
        else:
            print("Invalid choice.")

from data_access import DataAccess
from utilities import hash_password


class BusinessLogic:   
    def __init__(self):
        self.data_access = DataAccess() # Initialise data access layer

    def create_user(self, username, password, role):
        if not username or not password or not role:
            print("All fields are required.")
            return
        if role not in ["admin", "data_engineer", "user"]:
            print("Invalid role. Choose from 'admin', 'data_engineer', or 'user'.")
            return
        hashed_password = hash_password(password) #Hash the password
        self.data_access.add_user(username, hashed_password, role) #Add the user

    def authenticate_user(self, username, password):
        if not username or not password:
            print("Username and password are required.")
            return None
        user = self.data_access.get_user(username) #fetch the user
        if user and user[2] == hash_password(password):  #Check if password matches
            return user
        return None

    def list_users(self):
        return self.data_access.get_all_users() #fetch all uswers

    def execute_query(self, query):
        return self.data_access.run_custom_query(query)

    def run_data_pipeline(self):
        # Mock data pipeline logic
        print("Running data pipeline...")
        # Simulate some data processing steps
        print("Step 1: Extracting data...")
        print("Step 2: Transforming data...")
        print("Step 3: Loading data into the database...")
        print("Data pipeline executed successfully.")

    def add_data(self, content):
        if not content:
            print("Content cannot be empty.")
            return
        self.data_access.add_data(content) #add data

    def read_data(self, data_id):
        return self.data_access.read_data(data_id) #read data by id

    def update_data(self, data_id, new_content): #update data by id
        if not new_content:
            print("New content cannot be empty.")
            return
        self.data_access.update_data(data_id, new_content)

    def delete_data(self, data_id):
        self.data_access.delete_data(data_id) #delete data by id

#data_access.py
import sqlite3
from config import DATABASE_PATH


class DataAccess:
    def __init__(self):
        """Connection to the database"""
        try:
            self.conn = sqlite3.connect(DATABASE_PATH)
            self.create_tables() #create tables if they don't exist
        except sqlite3.Error as e:
            print(f"Database connection failed: {e}")
            raise

    def create_tables(self):
        
        try:
            with self.conn:
                self.conn.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    password TEXT,
                    role TEXT
                )''')
                self.conn.execute('''CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY,
                    content TEXT
                )''')
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
            raise

    def add_user(self, username, password, role):
        try:
            with self.conn:
                self.conn.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                            (username, password, role)) #add a new user and assign role
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")
            raise

    def get_user(self, username):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM users WHERE username=?", (username,)) #fetch uswer
            return cur.fetchone()
        except sqlite3.Error as e:
            print(f"Error fetching user: {e}")
            raise

    def get_all_users(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM users") #get all users
            return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching all users: {e}")
            raise

    def add_data(self, content):
        try:
            with self.conn:
                self.conn.execute("INSERT INTO data (content) VALUES (?)", (content,)) #add new data
        except sqlite3.Error as e:
            print(f"Error adding data: {e}")
            raise

    def read_data(self, data_id):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM data WHERE id=?", (data_id,)) #read data by ID
            return cur.fetchone()
        except sqlite3.Error as e:
            print(f"Error reading data: {e}")
            raise

    def update_data(self, data_id, new_content):
        try:
            with self.conn:
                self.conn.execute("UPDATE data SET content=? WHERE id=?", (new_content, data_id)) #update data content
        except sqlite3.Error as e:
            print(f"Error updating data: {e}")
            raise

    def delete_data(self, data_id):
        try:
            with self.conn:
                self.conn.execute("DELETE FROM data WHERE id=?", (data_id,)) #delete data
        except sqlite3.Error as e:
            print(f"Error deleting data: {e}")
            raise

    def run_custom_query(self, query):
        try:
            cur = self.conn.cursor()
            cur.execute(query) #execute your own query
            self.conn.commit()
            return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            raise

"""
Concerns of each component in the Task manager

"""


"""

Actor/User:
Concerns: The user's primary concern is to interact with the system to view data visualizations. 
They are responsible for initiating the process by logging in and requesting to view the data visualizations.
System:
Authentication: The system's concern is to authenticate the user upon login request.
Data Retrieval: Once authenticated, the system retrieves the data visualizations from the database.
Presentation: The system's responsibility is to present the retrieved data visualizations to the user in a user-friendly format.
Error Handling: It should handle any errors that occur during the authentication process or data retrieval process and provide appropriate feedback to the user.
Database:
Data Storage: The database's main concern is to store the data visualizations securely and efficiently.
Data Retrieval: It retrieves the requested data visualizations and sends them back to the system for presentation.
Data Security: Ensuring that only authorized users can access the stored data is a key concern of the database component.
Each component focuses on its specific responsibilities within the sequence of interactions, 
ensuring the successful completion of the "View Data Visualizations" use case while addressing their respective concerns.

"""
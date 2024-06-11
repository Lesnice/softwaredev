#todo_list.py
class TodoList:
    def __init__(self):
        #initialise an empty list to store tasks
        self.tasks =[]
    
    def add_task(self, task):
        
        #add a new task to the list
        self.tasks.append(task)
        
    def update_task(self, old_task, new_task):
        
        #Update an existing task in the list
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index]= new_task
            
    def remove_task(self, task):
        
        #Remove a task form the list
        
        if task in self.tasks:
            self.tasks.remove(task)
            
        
    
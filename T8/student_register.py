def register(num_students):
    try:
        
    #ask the user how many students are registering
        num_students = int(input("How many students are registering?:"))
    #open in write mode
        with open("reg_form.txt", "w") as file:
            
       #iterate through each student
            for i in range(1, num_students +1):
                student_id = input(f"Enter student ID {i}:  ")
           
           #write Id followed by dotted lines
                file.write(f"{student_id}\n{'-'*25|n}")
           
        print("Registration completed, confirm with the form reg_form.txt")
    
    except ValueError:
        print("please enter max number of students.")
    
    
    
if __name__ == "__register__":
    register()
        
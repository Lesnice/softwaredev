
class Adult():

    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour
        
    def can_drive(self, name, age):
        print(f"{self.name}  are old enough to drive")
              
class Child(Adult):
    def can_drive(self, name, age):
        print("You are too young to drive")
        
def main():
    #take user inputs name, age, haircolour and eyecolour
    name = input("what is your name? ")
    age = input("How old are you?")
    eye_colour = input("What is your eye colour? ")
    hair_colour = input("What is your hair colour?")

    if age >= 18:
        individual = Adult(name, age, hair_colour, eye_colour)
    else:
        individual = Child(name, age, hair_colour, eye_colour)
    
    individual.can_drive()
    
if __name__ == "__main__":
    main()
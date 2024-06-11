"""=====================================
Method overriding example
"""

class Animal:
    def make_sound(self):
        return "Generic animal noise"
    
class Dog(Animal):
    
    def make_sound(self):
        return "woof, woof"
    
    def fetch(self):
        retrun "Dog is fetching the ball"
        
class Cat(Animal):
    
    def make_sound(self):
        return "meow meow!"
    
    
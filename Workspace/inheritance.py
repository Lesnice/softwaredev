# class Animal:
#     def __init__(self, sound: str) -> None:
#         self.sound = sound
        
#     def make_sound(self) -> str:
#         return f"The {type(self).__name__} goes {self.sound}"
    
    
# ###subclass
# class Lion(Animal):
#     pass


# animal = Animal("Animal sound")
# lion = Lion("rawr")

# print(animal.make_sound())
# print(lion.make_sound())

class Animal:
    def __init__(self, sound: str) -> None:
        self.sound = sound
        
    def make_sound(self) -> str:
        return f"The {type(self).__name__} goes {self.sound}"
    
    
###subclass
class Lion(Animal):
    pass

class Canary(Animal):
    pass

class Goldfish(Animal):
    pass

animal = Animal("Animal sound")
lion = Lion("rawr")
bird = Canary("tweet") 
fish = Goldfish("blub")

# print(lion.make_sound())
# print(bird.make_sound())
# print(fish.make_sound())

class Lion(Animal):
    def make_sound(self):
        return f"The fierce lion let's out a big {self.sound}"
    
class Canary(Animal):
    def make_sound(self):
        sound = "the canary tries to impress his partner with a song from the soul."
        sound +=f"{self.sound}  {self.sound}  {self.sound}"
        return sound
    
class Goldfish(Animal):
    def make_sound(self):
        return f"{self.sound} {self.sound}  {self.sound}"
    
    
    animals =[Lion("rawr")]
#    def make_sound(self) -> str:
#     return f"The fierce lionn let's out a bi {self.sound}!!!!"  #overiding 


# animal = Animal("Animal sound")
# lion = Lion("rawr")

# print(animal.make_sound())
# print(lion.make_sound())


# ##overiding and super

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.grades =[]
        
    
# #####multiple inheritance

# class BaseClass:
#     #base class definition
#     pass
# class BaseClassA:
#     #base clase definition
    
# class SubClass(BaseClass, BaseClassA):
#     #subclass definition
#     pass
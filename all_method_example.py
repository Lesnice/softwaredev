class Animals:
    #class attribute
    
    home = "Kruger"
    
    #creating instance attributes and methods
    
    def __init__(self, species, age):
        self.species =species
        self.age = age
        
    #creating class methods
    
    @classmethod
    def animals_hoe(cls, home):
        cls.home = home
        
    #instance method
    
    def insta_method(self):
        #modify the class attribute
        self.home = "Sabi Sands"
        return f"Species: {self.species}, Age: {self.age}, Location: {self.home}"
    
    #static method
    @staticmethod
    def check_age(age):
        if age >5:
            return "adult"
        else:
            return "Not adult"
        
a1 = Animals("Lion", 4)

print(a1.insta_method())
print(a1.check_age(4))
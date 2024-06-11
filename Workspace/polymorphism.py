#polymorphism and inheritance

class Bird:
    def intro(self):
        print("There are many species of birds")
        
    def flight(self):
        print("Most birds can fly but some cannot.")
#inheritance
class robin(Bird):
    def flight(self):
        print ("Robins can fly!")
        
class ostrich(Bird):
    def ostrich(self):
        print("Ostriches can't fly!")
        
        
bird = Bird()
bird_robin = robin()
bird_ostrich = ostrich()

bird.intro()
bird.flight()        

bird_robin.intro()
bird_robin.flight() 


bird_ostrich.intro()
bird_ostrich.flight() 
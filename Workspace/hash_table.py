class Node:
    def __init__(self, key, value):
    self.key =Key
    self.value=value
    
    
    
    
class HashTable:
    
    def __init__(self, capacity =20):
        self.capacity = capacity
        self.size= 0
        self.buckets = np.empty(capacity.node)
    
    
    def ___hash(self, key):
        return (hash(key)) % self.capacity
    
    def set(self, key, value):
        #Hash the key of the pair
        
        index = self.___hash(key)
        
        #check if there is a collision
        
        node = self.buckets[index]
        
        if (node==None):
            self.buckets[index]=Node(key, value)
            self.size +=1
        else:
            
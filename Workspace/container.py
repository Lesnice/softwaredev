class ContactList:
    
    def __init__(self):
        self.contact_list = []
        
    def add_contact(self, contact):
        self.contact_list.append(contact)
        
        
    def __getitem__(self, key):
        return self.contact_list[key]
        
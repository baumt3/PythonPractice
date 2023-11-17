# Create the Person class
class Person:
    def __init__(self, name, address, telephone):
        # The constructor initializes a Person object with a name, address, and telephone number.
        # Using double underscores to make these attributes private.
        self.__name = name  
        self.__address = address 
        self.__telephone = telephone
    
    # Setter method to update the person's name.
    def set_name(self, name):
        self.__name = name
    
    # Setter method to update the person's address.
    def set_address(self, address):
        self.__address = address
        
     # Setter method to update the person's telephone number.
    def set_telephone(self, telephone):
        self.__telephone = telephone
    
     # Getter method to retrieve the person's name.
    def get_name(self):
        return self.__name
    
     # Getter method to retrieve the person's address.
    def get_address(self):
        return self.__address
    
    # Getter method to retrieve the person's telephone number.
    def get_telephone(self):
        return self.__telephone